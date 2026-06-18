import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏢 Company Analysis")

df = pd.read_csv("jobs.csv")

company_df = df["company"].value_counts().reset_index()
company_df.columns = ["Company", "Jobs"]

st.dataframe(company_df)

fig = px.bar(
    company_df,
    x="Company",
    y="Jobs",
    title="Top Hiring Companies"
)

st.plotly_chart(fig, use_container_width=True)