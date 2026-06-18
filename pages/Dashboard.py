```python
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

# Load data
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Convert salary column
df["salary_value"] = (
    df["salary"]
    .str.replace(" LPA", "", regex=False)
    .astype(float)
)

# Total Skills
all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

top_skill = pd.Series(all_skills).value_counts().idxmax()

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💼 Total Jobs",
        len(df)
    )

with col2:
    st.metric(
        "🏢 Companies",
        df["company"].nunique()
    )

with col3:
    st.metric(
        "💰 Avg Salary",
        f"{round(df['salary_value'].mean(),1)} LPA"
    )

with col4:
    st.metric(
        "🔥 Top Skill",
        top_skill
    )

st.divider()

# Company chart
company_df = (
    df["company"]
    .value_counts()
    .reset_index()
)

company_df.columns = ["Company", "Jobs"]

fig1 = px.bar(
    company_df,
    x="Company",
    y="Jobs",
    color="Jobs",
    title="Top Hiring Companies"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Skills chart
skill_df = (
    pd.Series(all_skills)
    .value_counts()
    .reset_index()
)

skill_df.columns = ["Skill", "Demand"]

fig2 = px.bar(
    skill_df,
    x="Skill",
    y="Demand",
    color="Demand",
    title="Top Skills Demand"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.success("Dashboard loaded successfully 🚀")
```
