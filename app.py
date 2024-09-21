import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Vehicle Data Analysis")

st.subheader("Price Distribution")
fig_hist = px.histogram(df, x='price', nbins=30, title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist)

st.subheader("Price vs Odometer")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title="Price vs Odometer by Condition")
st.plotly_chart(fig_scatter)

if st.checkbox("Show only cars with price less than $20,000"):
    filtered_df = df[df['price'] < 20000]
    fig_filtered = px.scatter(filtered_df, x='odometer', y='price', color='condition', title="Filtered: Price vs Odometer (Under $20,000)")
    st.plotly_chart(fig_filtered)