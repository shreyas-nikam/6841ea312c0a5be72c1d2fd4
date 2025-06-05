
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from application_pages.page1 import run_page1
from application_pages.page2 import run_page2

st.set_page_config(page_title="Investment Base Pairs Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Investment Base Pairs Lab")
st.divider()

st.markdown("This lab explores Investment Base Pairs.")

page = st.sidebar.selectbox(label="Navigation", options=["Data Exploration", "Performance Analysis"])

if page == "Data Exploration":
    run_page1()
elif page == "Performance Analysis":
    run_page2()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
