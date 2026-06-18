
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Company Analysis",
    page_icon="🏢",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🏢 Company Analysis")
st.caption("Top hiring companies in the market")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("jobs.csv")

# ---------------- COMPANY STATS ----------------
company_df = df["company"].value_counts().reset_index()
company_df.columns = ["Company", "Jobs"]

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Companies",
        company_df["Company"].nunique()
    )

with col2:
    st.metric(
        "Total Jobs",
        company_df["Jobs"].sum()
    )

st.divider()

# Table
st.subheader("Company Overview")

st.dataframe(
    company_df,
    use_container_width=True
)

# Chart
fig = px.bar(
    company_df,
    x="Company",
    y="Jobs",
    title="Top Hiring Companies"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success("Company Analysis Loaded Successfully 🚀")

