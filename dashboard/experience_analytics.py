import streamlit as st
import pandas as pd
import os
import sys


def app():

    st.title("User Experience Analysis")

    df_avg_top10_tcp = pd.read_csv('../data/top_10_avg_tpc_ul.csv')
    df_avg_top10_rrt = pd.read_csv('../data/top_10_avg_rtt_ul.csv')
    avg_thr = pd.read_csv('../data/avg_throughput.csv')
    avg_tcp = pd.read_csv('../data/avg_tcp.csv')

    st.header("Top 10 Users Experience analysis")
    st.subheader("Average TCP UL (Bytes)")
    st.dataframe(df_avg_top10_tcp)
    st.bar_chart(df_avg_top10_tcp['TCP UL Retrans. Vol (Bytes)'])

    st.subheader("Avg UL Time")
    st.dataframe(df_avg_top10_rrt)
    st.bar_chart(df_avg_top10_rrt['Avg RTT UL (ms)'])

    st.header("Most Frequenct")
    st.subheader('Frquent Average Throughput')
    st.dataframe(avg_thr)
    st.bar_chart(avg_thr['Handset Type'])

    st.subheader("Average TCP")
    st.dataframe(avg_tcp)
    st.bar_chart(avg_tcp['Handset Type'])

    st.header("Cluster with 3 group classification")
    st.image('../data/cluster_classife.png')


# Run the Streamlit app
if __name__ == '__main__':
    app()
