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
    st.title("User Engagement Analysis")

    # Load DataFrames
    df_customer = pd.read_csv('../data/top_10_handset.csv')
    # Display Heatmap
    st.header("Heatmap of Unit Sales for Top 10 Handsets")
    heatmap_data = df_customer.pivot_table(
        values='Unit Solds', index='index', aggfunc='sum')
    st.pyplot(create_heatmap(heatmap_data))


def create_heatmap(heatmap_data):
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='viridis',
                annot=True, fmt='g', linewidths=.5)
    plt.title("Heatmap of Unit Sales for Top 10 Handsets")
    plt.xlabel("Handset Type")
    plt.ylabel("Unit Sold")

    # Return the figure to be displayed by Streamlit
    st.pyplot(plt.gcf())

    # Close the figure explicitly
    plt.close()


# Run the Streamlit app
if __name__ == '__main__':
    app()
