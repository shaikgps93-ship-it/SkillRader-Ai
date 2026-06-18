import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔥 Skills Analysis")

df = pd.read_csv("jobs.csv")

all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

skill_df = pd.Series(all_skills).value_counts().reset_index()
skill_df.columns = ["Skill", "Demand"]

st.dataframe(skill_df)

fig = px.bar(
    skill_df,
    x="Skill",
    y="Demand",
    title="Top Skills Demand"
)

st.plotly_chart(fig, use_container_width=True)