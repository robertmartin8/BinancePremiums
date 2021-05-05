import time
from datetime import datetime as dt
import os
import re
import streamlit as st
from data_downloader import get_coin_fut_premiums, get_coin_perp_funding


def markdown_content(filename):
    with open(f"content/{filename}.md") as f:
        s = f.read()

        return st.markdown(s, unsafe_allow_html=True)


# Modify streamlit code
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-G-MZ1Z0ZNKDE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-G-MZ1Z0ZNKDE');
</script>"""

index_file = os.path.dirname(st.__file__) + "/static/index.html"
with open(index_file, "r") as f:
    data = f.read()
    if len(re.findall("UA-", data)) == 0:
        with open(index_file, "w") as ff:
            newdata = re.sub("<head>", "<head>" + code, data)
            ff.write(newdata)

js_file_dir = os.path.dirname(st.__file__) + "/static/static/js"
js_file = [
    i for i in os.listdir(js_file_dir) if i.startswith("main") and i.endswith(".js")
][0]
js_file = js_file_dir + "/" + js_file
with open(js_file, "r") as f:
    data = f.read()
    regex1 = r'document.title="".concat\(t," \\xb7 Streamlit"\)'
    if len(re.findall(regex1, data)) != 0:
        with open(js_file, "w") as ff:
            newdata = re.sub(
                regex1,
                'document.title="".concat(t,"")',
                data,
            )
            ff.write(newdata)

    regex2 = r'document.title="".concat\(s," \\xb7 Streamlit"\)'
    if len(re.findall(regex2, data)) != 0:
        with open(js_file, "w") as ff:
            newdata = re.sub(
                regex2,
                'document.title="".concat(s,"")',
                data,
            )
            ff.write(newdata)

st.set_page_config(page_title="BinancePremiums", page_icon=":chart_with_upwards_trend:")

# .reportview-container .main .block-container{{
#     max-width: 50%;
#     padding-right: 0rem;
#     padding-left: 0rem;
#     padding-bottom: 3rem;
# }}


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
