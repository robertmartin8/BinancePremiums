import streamlit as st
from datetime import datetime as dt
import pandas as pd
import requests
from binance.client import Client

client = Client()


def get_coin_fut_symbols():
    """
    Symbols for coin-margined delivery
    """
    coin_info = client.futures_coin_exchange_info()
    fut_symbols = [
        c["symbol"]
        for c in coin_info["symbols"]
        if c["contractType"] != "PERPETUAL" and c["contractStatus"] == "TRADING"
    ]
    perp_symbols = [
        c["symbol"]
        for c in coin_info["symbols"]
        if c["contractType"] == "PERPETUAL" and c["contractStatus"] == "TRADING"
    ]
    return fut_symbols, perp_symbols


def get_fut_symbols():
    fut_info = client.futures_exchange_info()
    fut_symbols = [
        c["symbol"]
        for c in fut_info["symbols"]
        if c["contractType"] != "PERPETUAL" and c["status"] == "TRADING"
    ]
    perp_symbols = [
        c["symbol"]
        for c in fut_info["symbols"]
        if c["contractType"] == "PERPETUAL" and c["status"] == "TRADING"
    ]
    return fut_symbols, perp_symbols


@st.cache(ttl=310, allow_output_mutation=True)
def get_coin_fut_premiums(timestamp=None):
    r = requests.get("https://dapi.binance.com/dapi/v1/premiumIndex")
    d = r.json()
    df = pd.DataFrame(d)
    df = df[~df.symbol.str.contains("PERP")]
    df["exp"] = df.symbol.str.split("_").str[-1]
    df = df[["pair", "markPrice", "indexPrice", "exp"]]
    df[["markPrice", "indexPrice"]] = df[["markPrice", "indexPrice"]].astype(float)

    df["exp"] = pd.to_datetime(df.exp, format="%y%m%d").map(
        lambda x: dt(x.year, x.month, x.day, 8)
    )
    seconds_to_expiry = (df.exp - dt.utcnow()).dt.total_seconds()
    compound = 365 * 24 * 3600 / seconds_to_expiry
    df["dte"] = seconds_to_expiry / (24 * 3600)
    df["premium"] = df.markPrice / df.indexPrice - 1
    # df["premium_ann"] = df.premium / (df.dte / 365)
    df["premium_ann"] = (1 + df.premium) ** compound - 1
    df = (
        df.drop("exp", axis=1)
        .sort_values(by="premium_ann", ascending=False)
        .reset_index(drop=True)
    )

    # Clean up and style
    df.columns = [
        "Pair",
        "Future Price",
        "Spot Price",
        "Expiry",
        "Premium",
        "Premium (ann.)",
    ]

    df_styled = df.style.format(
        {
            "Future Price": "{:.3f}",
            "Spot Price": "{:.3f}",
            "Expiry": "{:.1f} days",
            "Premium": "{:.2%}",
            "Premium (ann.)": "{:.2%}",
        }
    )
    return df_styled


@st.cache(ttl=310, allow_output_mutation=True)
def get_coin_perp_funding(timestamp=None):
    fut_info = client.futures_coin_exchange_info()
    perp_symbols = [
        c["symbol"]
        for c in fut_info["symbols"]
        if c["contractType"] == "PERPETUAL" and c["contractStatus"] == "TRADING"
    ]

    res = []
    for symbol in perp_symbols:
        d = client.futures_coin_funding_rate(symbol=symbol)
        funding_rates = [float(i["fundingRate"]) for i in d]
        last = funding_rates[-1]
        avg_7 = sum(funding_rates[-7 * 3 :]) / (7 * 3)
        avg_14 = sum(funding_rates[-14 * 3 :]) / (14 * 3)
        avg_30 = sum(funding_rates[-30 * 3 :]) / (30 * 3)
        res.append((d[-1]["symbol"], last, avg_7, avg_14, avg_30))

    df = pd.DataFrame(
        res,
        columns=[
            "symbol",
            "last",
            "avg_7d",
            "avg_14d",
            "avg_30d",
        ],
    )

    # use more recent data for last
    r = requests.get("https://dapi.binance.com/dapi/v1/premiumIndex")
    d = r.json()
    df1 = pd.DataFrame(d)
    df1 = (
        df1[df1.symbol.str.contains("PERP")][["symbol", "lastFundingRate"]]
        .set_index("symbol")
        .astype(float)
    )
    df["last"] = df1.reindex(df.symbol).values

    # Annualise
    df.iloc[:, 1:] = (1 + df.iloc[:, 1:]) ** (365 * 3) - 1
    df = df.sort_values(by="last", ascending=False).reset_index(drop=True)

    # Clean up and style
    df.columns = [
        "Pair",
        "Last",
        "7d avg",
        "14d avg",
        "30d avg",
    ]

    df_styled = df.style.format(
        {
            "Last": "{:.2%}",
            "7d avg": "{:.2%}",
            "14d avg": "{:.2%}",
            "30d avg": "{:.2%}",
        }
    )
    return df_styled
