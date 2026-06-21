
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Salary Insights",
    page_icon="💰",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("💰 Salary Insights")
st.caption("Explore salary trends and distributions")

# ---------------- LOAD DATA ----------------
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ---------------- CLEAN SALARY ----------------
df["salary_value"] = (
    df["salary"]
    .str.replace(" LPA", "", regex=False)
    .astype(float)
)

# ---------------- METRICS ----------------
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

st.divider()

# ---------------- DISTRIBUTION ----------------
st.subheader("Salary Distribution")

fig = px.histogram(
    df,
    x="salary_value",
    nbins=10,
    title="Salary Distribution"
)

fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- TOP SALARIES ----------------
st.subheader("Top Paying Roles")

top_salary_df = df.sort_values(
    "salary_value",
    ascending=False
)

st.dataframe(
    top_salary_df,
    use_container_width=True
)

st.success("Salary Insights Loaded Successfully 🚀")

