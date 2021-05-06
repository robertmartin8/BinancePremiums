import os
import streamlit as st
import re

# Modify streamlit code
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-G-0Y175Y9Y6G"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-G-0Y175Y9Y6G');
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
