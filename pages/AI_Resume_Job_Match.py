import streamlit as st
import pandas as pd
import sqlite3
from PyPDF2 import PdfReader

st.title("🤖 AI Resume + Job Match Engine")

# Load jobs data
conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM jobs", conn)
conn.close()

# Build market skill list
all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

market_skills = set(all_skills)

# Upload resume
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

target_role = st.selectbox(
    "Target Role",
    [
        "Data Analyst",
        "Data Engineer",
        "BI Analyst",
        "Data Scientist"
    ]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    found_skills = []

    for skill in market_skills:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    match_score = (
        len(found_skills) /
        len(market_skills)
    ) * 100

    st.metric(
        "Resume Match Score",
        f"{match_score:.0f}%"
    )

    st.subheader("✅ Skills Found")

    for skill in found_skills:
        st.success(skill)

    missing_skills = market_skills - set(found_skills)

    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.warning(skill)

    st.subheader("🚀 Recommendation")

    if len(missing_skills) > 0:

        recommendation = ", ".join(
            list(missing_skills)[:3]
        )

        st.info(
            f"Learn {recommendation} to improve your profile."
        )