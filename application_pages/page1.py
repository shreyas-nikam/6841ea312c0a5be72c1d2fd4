
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Data Exploration")
    data = pd.DataFrame({
        'Asset Class': ['Equities', 'Bonds', 'Currencies', 'Commodities'] * 3,
        'Signal Type': ['Value', 'Momentum', 'Carry'] * 4,
        'Return': [0.1, 0.05, 0.15, 0.12, 0.08, 0.18, 0.09, 0.06, 0.14, 0.1, 0.07, 0.16, 0.11, 0.04, 0.17],
        'Volatility': [0.1, 0.08, 0.12, 0.09, 0.06, 0.15, 0.07, 0.05, 0.11, 0.08, 0.09, 0.13, 0.07, 0.03, 0.14],
        'Sharpe Ratio': [1.0, 0.625, 1.25, 1.33, 1.33, 1.2, 1.28, 1.2, 1.27, 1.25, 0.77, 1.23, 1.57, 1.33, 1.21],
        'Own-asset Predictability': [0.5, 0.4, 0.6, 0.55, 0.45, 0.65, 0.5, 0.35, 0.6, 0.48, 0.38, 0.62, 0.52, 0.42, 0.68],
        'Cross-asset Predictability': [0.3, 0.2, 0.4, 0.35, 0.25, 0.45, 0.3, 0.15, 0.4, 0.28, 0.18, 0.42, 0.32, 0.22, 0.48],
        'Signal Correlation': [0.6, 0.5, 0.7, 0.65, 0.55, 0.75, 0.6, 0.45, 0.7, 0.58, 0.48, 0.72, 0.62, 0.52, 0.78],
        'Signal Mean Imbalance': [0.1, 0.05, 0.15, 0.12, 0.08, 0.18, 0.09, 0.06, 0.14, 0.1, 0.07, 0.16, 0.11, 0.04, 0.17],
        'Signal Variance Imbalance': [0.2, 0.1, 0.3, 0.25, 0.15, 0.35, 0.2, 0.1, 0.3, 0.18, 0.12, 0.32, 0.22, 0.12, 0.38],
        'Unexplained Effect': [0.05, 0.02, 0.08, 0.07, 0.04, 0.1, 0.05, 0.03, 0.06, 0.06, 0.03, 0.09, 0.08, 0.01, 0.11]
    })
    st.dataframe(data)
    asset_class = st.selectbox("Select Asset Class", data['Asset Class'].unique())
    filtered_data = data[data['Asset Class'] == asset_class]
    fig = px.scatter(filtered_data, x="Return", y="Volatility", hover_data=['Signal Type'])
    st.plotly_chart(fig)
