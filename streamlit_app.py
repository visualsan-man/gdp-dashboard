import streamlit as st
import pandas as pd
import math
from pathlib import Path
from io import StringIO

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
       )
# -----------------------------------------------------------------------------
# Declare some useful functions.

image=st.camera_input("carmea image")
if image is not None:
    st.image(image)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
