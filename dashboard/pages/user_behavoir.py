import streamlit.components.v1 as components
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from streamlit import components
import os


def app():
    st.subheader("User Behavoir Analysis")
    feq = pd.read_csv('../data/top_10_customer_with_frq.csv')
    duration = pd.read_csv('../data/top_10_customer_duration.csv')
    # Create a sidebar menu
    selected_option = st.sidebar.selectbox(
        "Data Frame for Top 10 Customer ", ["Session Frequceny", "Duration"])

    # Display the selected data in the main content area
    if selected_option == "Session Frequceny":
       # Streamlit App
        st.title('Top 10 Customers with Frequency')
        # Display the DataFrame in the Streamlit app
        st.dataframe(feq)
    elif selected_option == "Duration":
        # Streamlit App
        st.title('Top 10 Customers with Duration')
        # Display the DataFrame in the Streamlit app
        st.dataframe(duration)

    st.header("Heatmap of Unit Sales for Top 10 Handsets")
    st.image('../data/heatmap_sales.png')

    st.subheader(
        "Distribution of Unit Sales Among Top 3 Headset Manufacturers")
    st.image('../data/pie_chart_top_3_headset.png')

    st.subheader(
        "Top 10 Customers with Highest Session Duration")
    st.image('../data/top_10_customer_highest_session.png')

    st.subheader(
        "Correlation Heatmap for Selected Columns")
    st.image('../data/correlation_totdl_toul_totsession.png')
    st.subheader(
        "Correlation Heatmap for Selected Columns")
    st.image('../data/top_3_apps_by_10_users.png')
