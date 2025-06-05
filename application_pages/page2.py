
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page2():
    st.header("Performance Analysis")
    data = {'Driver': ['Own-asset', 'Cross-asset', 'Correlation', 'Mean Imbalance', 'Variance Imbalance', 'Unexplained'],
            'Contribution': [0.3, 0.15, 0.2, 0.1, 0.1, 0.15]}
    df = pd.DataFrame(data)
    fig = px.bar(df, x='Driver', y='Contribution', title='Contribution of Key Drivers')
    st.plotly_chart(fig)

