import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Satisfaction Analysis")

    st.header("User Clustering based on both scores")
    st.image('../data/score_cluster.png')
    st.markdown(
        'We can boost customer happiness by increasing the **experience score**.')


# Run the Streamlit app
if __name__ == '__main__':
    app()
