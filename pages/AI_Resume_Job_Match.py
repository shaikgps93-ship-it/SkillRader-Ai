import streamlit as st

col1, col2 = st.columns([8,1])

with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
import streamlit as st
import sqlite3
import pandas as pd
from PyPDF2 import PdfReader
import plotly.graph_objects as go

st.title("🤖 AI Resume + Job Match Engine")

# Load jobs database
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Build market skills
all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

market_skills = set(all_skills)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    # Find skills
    found_skills = []

    for skill in market_skills:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    missing_skills = market_skills - set(found_skills)

    # Score
    score = int(
        (len(found_skills) / len(market_skills)) * 100
    )

    st.subheader("🎯 ATS Match Score")

    st.progress(score / 100)

    st.metric(
        "Resume Match",
        f"{score}%"
    )

    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Resume Strength"},
        gauge={
            "axis": {"range": [0, 100]}
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Skills Found
    st.subheader("✅ Skills Found")

    for skill in found_skills:
        st.success(skill)

    # Missing Skills
    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.warning(skill)

    # Recommendations
    st.subheader("🚀 Recommendations")

    for skill in list(missing_skills)[:3]:
        st.info(f"Learn {skill}")
