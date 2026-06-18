
import streamlit as st
import sqlite3
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Job Recommendation",
    page_icon="🚀",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🚀 Job Recommendation Engine")
st.caption("Find jobs matching your skills")

# ---------------- LOAD JOBS ----------------
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    user_skills = st.text_input(
        "Enter Your Skills",
        "SQL, Python"
    )

with col2:
    experience = st.slider(
        "Years of Experience",
        1,
        10,
        2
    )

# ---------------- FIND MATCHES ----------------
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

    # Metrics
    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Jobs Found",
            len(result_df)
        )

    with c2:
        st.metric(
            "Best Match",
            f"{result_df['Match Score'].max()}%"
        )

    st.divider()

    st.dataframe(
        result_df,
        use_container_width=True
    )

    st.success("Job Recommendations Generated 🚀")

