import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("💰 Salary Insights")

# Load data
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Convert salary column to numeric
df["salary_value"] = (
    df["salary"]
    .str.replace(" LPA", "", regex=False)
    .astype(float)
)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Salary",
        f"{df['salary_value'].mean():.1f} LPA"
    )

with col2:
    st.metric(
        "Highest Salary",
        f"{df['salary_value'].max():.1f} LPA"
    )

with col3:
    st.metric(
        "Lowest Salary",
        f"{df['salary_value'].min():.1f} LPA"
    )

# Salary distribution chart
st.subheader("Salary Distribution")

fig = px.histogram(
    df,
    x="salary_value",
    nbins=5,
    title="Salary Distribution"
)

st.plotly_chart(fig, use_container_width=True)