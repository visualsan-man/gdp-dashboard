import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)
st.header("翡翠开料王软件")
st.text('''
本项目致力于开发一个翡翠及玉石自动排版APP
采用AI算法自动对布局排版出图。
'''
# -----------------------------------------------------------------------------
# Declare some useful functions.

