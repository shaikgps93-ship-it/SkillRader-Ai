
import streamlit as st
import pandas as pd
import sqlite3
from PyPDF2 import PdfReader

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume Match Score",
    page_icon="🎯",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🎯 Resume Match Score")
st.caption("Measure your resume against market skills")

# ---------------- LOAD JOBS ----------------
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ---------------- MARKET SKILLS ----------------
all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

market_skills = set(all_skills)

# ---------------- UPLOAD RESUME ----------------
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
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

    missing_skills = market_skills - set(found_skills)

    score = int(
        (len(found_skills) / len(market_skills)) * 100
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Resume Score",
            f"{score}%"
        )

    with c2:
        st.metric(
            "Skills Found",
            len(found_skills)
        )

    with c3:
        st.metric(
            "Missing Skills",
            len(missing_skills)
        )

    st.progress(score / 100)

    st.divider()

    # Skills Found
    st.subheader("✅ Skills Found")

    for skill in found_skills:
        st.success(skill)

    # Missing Skills
    st.subheader("❌ Missing Skills")

    for skill in list(missing_skills)[:10]:
        st.warning(skill)

    st.success("Resume Match Analysis Completed 🚀")

