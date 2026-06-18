import streamlit as st
import pandas as pd

st.title("🎯 Skill Gap Analyzer")

df = pd.read_csv("jobs.csv")

all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

market_skills = set(all_skills)

user_skills = st.text_input(
    "Enter your skills separated by commas",
    "SQL, Excel"
)

my_skills = set(
    [skill.strip() for skill in user_skills.split(",")]
)

missing_skills = market_skills - my_skills

st.write("## Missing Skills")

for skill in missing_skills:
    st.success(skill)
