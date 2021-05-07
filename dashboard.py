import time
from datetime import datetime as dt
import os
import re
import streamlit as st
from streamlit import caching
from data_downloader import get_coin_fut_premiums, get_coin_perp_funding


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

delivery_premiums_table = st.empty()
u0 = st.empty()

markdown_content("perpetuals_funding1")

perp_funding_table = st.empty()
u1 = st.empty()

markdown_content("futures_premiums2")
markdown_content("perpetuals_funding2")
markdown_content("explainer")
markdown_content("risks")
markdown_content("about")

RELOAD_INTERVAL_MINS = 5
counter = 0
while True:
    timestamp = dt.utcnow()
    caching.clear_cache()
    error_message = "Error loading data. Please refresh the page or try again later."
    try:
        delivery_premiums_table.dataframe(get_coin_fut_premiums(timestamp))
    except:
        delivery_premiums_table.error(error_message)
    try:
        perp_funding_table.dataframe(get_coin_perp_funding(timestamp))
    except:
        perp_funding_table.error(error_message)

    for u in [u0, u1]:
        u.text(
            f"Last updated: UTC {timestamp}. Updated every {RELOAD_INTERVAL_MINS} minutes"
        )
    time.sleep(RELOAD_INTERVAL_MINS * 60)
