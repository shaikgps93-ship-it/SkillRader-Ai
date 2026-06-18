import streamlit as st
import sqlite3
import pandas as pd

st.title("🎯 Job Recommendation Engine")

# Load jobs
conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM jobs", conn)
conn.close()

user_skills = st.text_input(
    "Enter your skills",
    "SQL, Python"
)

experience = st.slider(
    "Years of Experience",
    1,
    10,
    2
)

if st.button("Find Matching Jobs"):

    user_skill_set = set(
        skill.strip().lower()
        for skill in user_skills.split(",")
    )

    recommendations = []

    for _, row in df.iterrows():

        job_skill_set = set(
            skill.strip().lower()
            for skill in row["skills"].split(",")
        )

        matched_skills = user_skill_set.intersection(job_skill_set)

        score = (
            len(matched_skills)
            / len(job_skill_set)
        ) * 100

        recommendations.append({
            "Company": row["company"],
            "Role": row["title"],
            "Match Score": round(score, 0)
        })

    result_df = pd.DataFrame(recommendations)

    result_df = result_df.sort_values(
        "Match Score",
        ascending=False
    )

    st.dataframe(result_df)