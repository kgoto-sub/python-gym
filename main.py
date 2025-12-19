import pathlib
import random
import re

import streamlit as st

EXERCESE_ROOT = "./exercises"

file = random.choice([f for f in pathlib.Path(EXERCESE_ROOT).iterdir() if f.is_file()])

with open(file, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"^#\s+(.+?)\n(.*?)(?=\n#\s+|\Z)"
matches = re.findall(pattern, content, flags=re.MULTILINE | re.DOTALL)

content_dict = {title.strip(): body.strip() for title, body in matches}

st.header("問題")
st.markdown(content_dict["問題"])

if st.button("模範回答を表示"):
    st.header("模範回答")
    st.code(content_dict["模範解答"], language="python")

if st.button("次の問題へ"):
    st.rerun()
