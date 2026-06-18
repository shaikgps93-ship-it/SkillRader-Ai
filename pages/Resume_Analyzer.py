
import streamlit as st
import requests
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Live Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Home Button
if st.button("🏠 Home"):
    st.switch_page("app.py")

st.title("📄 Live Resume Analyzer")
st.caption("Match your resume against live job market skills")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    # Extract Resume Text
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text

    resume_text = resume_text.lower()

    market_skills = set()

    # ---------------- RemoteOK ----------------
    try:

        response = requests.get(
            "https://remoteok.com/api",
            headers={"User-Agent": "Mozilla/5.0"}
        )

        jobs = response.json()[1:]

        for job in jobs:

            tags = job.get("tags", [])

            for tag in tags:
                market_skills.add(tag.lower())

    except:
        pass

    # ---------------- Skill Matching ----------------
    found_skills = []

    for skill in market_skills:

        if skill in resume_text:
            found_skills.append(skill)

    missing_skills = market_skills - set(found_skills)

    score = int(
        (len(found_skills) / max(len(market_skills), 1)) * 100
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Resume Score", f"{score}%")

    with c2:
        st.metric("Skills Found", len(found_skills))

    with c3:
        st.metric("Missing Skills", len(missing_skills))

    st.progress(score / 100)

    st.divider()

    st.subheader("✅ Skills Found")

    for skill in sorted(found_skills):
        st.success(skill)

    st.subheader("❌ Top Missing Skills")

    for skill in sorted(list(missing_skills))[:15]:
        st.warning(skill)

    st.subheader("🚀 Suggested Next Skills")

    for skill in sorted(list(missing_skills))[:5]:
        st.info(f"Learn {skill}")

