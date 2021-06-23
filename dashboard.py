import time
from datetime import datetime as dt
import os
import re
import streamlit as st
from streamlit import caching
from data_downloader import (
    get_coin_fut_premiums,
    get_coin_perp_funding,
    get_usd_fut_premiums,
    get_usd_perp_funding,
)


def markdown_content(filename):
    with open(f"content/{filename}.md") as f:
        s = f.read()

        return st.markdown(s, unsafe_allow_html=True)


st.set_page_config(page_title="BinancePremiums", page_icon=":chart_with_upwards_trend:")

st.markdown(
    f"""
<style>

    .reportview-container .main .block-container{{
        padding-top: 3rem;
        padding-bottom: 3rem;
    }}
    div[data-testid="stToolbar"] {{visibility: hidden;}}
    footer {{visibility: hidden;}}
</style>
""",
    unsafe_allow_html=True,
)

markdown_content("intro")

markdown_content("futures_premiums1")

st.markdown("### Coin-margined")
delivery_premiums_table = st.empty()
u0 = st.text("Loading")

st.markdown("### USD-margined")
delivery_premiums_usd_table = st.empty()
u1 = st.text("Loading...")

markdown_content("perpetuals_funding1")

st.markdown("### Coin-margined")
perp_funding_table = st.empty()
u2 = st.text("Loading...")

st.markdown("### USD-margined")
perp_funding_usd_table = st.empty()
u3 = st.text("Loading...")


markdown_content("futures_premiums2")
markdown_content("perpetuals_funding2")
markdown_content("explainer")
markdown_content("risks")
markdown_content("about")

error_message = "Error loading data. Please refresh the page or try again later."
RELOAD_INTERVAL_MINS = 5
counter = 0
while True:
    timestamp = dt.utcnow()
    update_text = (
        f"Last updated: UTC {timestamp}. Updated every {RELOAD_INTERVAL_MINS} minutes"
    )
    caching.clear_cache()
    try:
        delivery_premiums_table.dataframe(get_coin_fut_premiums(timestamp))
        u0.text(update_text)
    except:
        delivery_premiums_table.error(error_message)
    try:
        delivery_premiums_usd_table.dataframe(get_usd_fut_premiums(timestamp))
        u1.text(update_text)
    except:
        delivery_premiums_usd_table.error(error_message)
    try:
        perp_funding_table.dataframe(get_coin_perp_funding(timestamp))
        u2.text(update_text)
    except:
        perp_funding_table.error(error_message)
    try:
        perp_funding_usd_table.dataframe(get_usd_perp_funding(timestamp))
        u3.text(update_text)
    except:
        perp_funding_usd_table.error(error_message)

    time.sleep(RELOAD_INTERVAL_MINS * 60)
