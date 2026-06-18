import streamlit as st
import pandas as pd
import sqlite3
from PyPDF2 import PdfReader

st.title("🎯 Resume Match Score")

# Load jobs data
conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT * FROM jobs", conn)
conn.close()

# Extract market skills
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

    score = (len(found_skills) / len(market_skills)) * 100

    st.metric(
        "Resume Match Score",
        f"{score:.0f}%"
    )

    st.subheader("✅ Skills Found")
    st.success(", ".join(found_skills))

    missing = market_skills - set(found_skills)

    st.subheader("❌ Missing Skills")

    for skill in missing:
        st.warning(skill)