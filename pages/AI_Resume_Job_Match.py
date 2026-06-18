import streamlit as st
import sqlite3
import pandas as pd
from PyPDF2 import PdfReader
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI Resume Match",
    page_icon="🤖",
    layout="wide"
)

# Home Button
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

st.title("🤖 AI Resume + Job Match Engine")
st.caption("Analyze resume skills against market demand")

# Load jobs
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Market skills
all_skills = []

for skills in df["skills"]:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

market_skills = set(all_skills)

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

    found_skills = []

    for skill in market_skills:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    missing_skills = market_skills - set(found_skills)

    score = int(
        (len(found_skills) / len(market_skills)) * 100
    )

    st.progress(score / 100)

    st.metric(
        "Resume Match",
        f"{score}%"
    )

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

    st.subheader("✅ Skills Found")

    for skill in found_skills:
        st.success(skill)

    st.subheader("❌ Missing Skills")

    for skill in list(missing_skills)[:10]:
        st.warning(skill)

    st.subheader("🚀 Recommendations")

    for skill in list(missing_skills)[:3]:
        st.info(f"Learn {skill}")
