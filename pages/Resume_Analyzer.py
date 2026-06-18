
import streamlit as st
import requests
from PyPDF2 import PdfReader

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8, 1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("📄 Live Resume Analyzer")
st.caption("Analyze your resume against live market demand")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    # ------------------------------------
    # Extract Resume Text
    # ------------------------------------
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text

    resume_text = resume_text.lower()

    # ------------------------------------
    # Fetch Live Market Skills
    # ------------------------------------
    market_skills = set()

    try:

        response = requests.get(
            "https://remoteok.com/api",
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        jobs = response.json()[1:]

        for job in jobs:

            tags = job.get("tags", [])

            for tag in tags:
                market_skills.add(tag.lower())

    except:

        st.warning("Unable to fetch live jobs.")

    # ------------------------------------
    # Match Skills
    # ------------------------------------
    found_skills = []

    for skill in market_skills:

        if skill in resume_text:
            found_skills.append(skill)

    missing_skills = market_skills - set(found_skills)

    score = int(
        (len(found_skills) / max(len(market_skills), 1)) * 100
    )

    # ------------------------------------
    # METRICS
    # ------------------------------------
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🎯 ATS Score",
            f"{score}%"
        )

    with c2:
        st.metric(
            "✅ Skills Found",
            len(found_skills)
        )

    with c3:
        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )

    st.progress(score / 100)

    # ------------------------------------
    # Resume Strength
    # ------------------------------------
    if score >= 80:

        st.success("🟢 Strong Resume")

    elif score >= 60:

        st.warning("🟡 Good Resume")

    else:

        st.error("🔴 Resume Needs Improvement")

    st.divider()

    # ------------------------------------
    # Career Match
    # ------------------------------------
    st.subheader("💼 Career Match")

    st.progress(0.92, text="Data Analyst")
    st.progress(0.84, text="BI Analyst")
    st.progress(0.75, text="Business Analyst")
    st.progress(0.70, text="Data Engineer")

    st.divider()

    # ------------------------------------
    # Skills Found
    # ------------------------------------
    st.subheader("✅ Skills Detected")

    cols = st.columns(3)

    for i, skill in enumerate(sorted(found_skills)):

        with cols[i % 3]:

            st.success(skill)

    # ------------------------------------
    # Missing Skills
    # ------------------------------------
    st.divider()

    st.subheader("🚀 Recommended Skills")

    cols = st.columns(3)

    for i, skill in enumerate(sorted(list(missing_skills))[:15]):

        with cols[i % 3]:

            st.warning(f"Learn {skill}")

    # ------------------------------------
    # Free Resources
    # ------------------------------------
    st.divider()

    st.subheader("📚 Free Learning Resources")

    st.link_button(
        "Python Course",
        "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
    )

    st.link_button(
        "SQL Tutorial",
        "https://www.w3schools.com/sql/"
    )

    st.link_button(
        "SQL Practice",
        "https://www.hackerrank.com/domains/sql"
    )

    st.link_button(
        "Power BI Learning",
        "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"
    )

    st.success("Resume Analysis Completed Successfully 🚀")
