
import streamlit as st
from PyPDF2 import PdfReader

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ATS Resume Score",
    page_icon="🎯",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8, 1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🎯 ATS Resume Score")
st.caption("Compare your resume against a job description")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if uploaded_file and job_description:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            resume_text += text

    resume_text = resume_text.lower()
    jd_text = job_description.lower()

    jd_keywords = set(jd_text.split())
    resume_keywords = set(resume_text.split())

    matched = jd_keywords.intersection(resume_keywords)
    missing = jd_keywords - resume_keywords

    score = int(
        (len(matched) / max(len(jd_keywords), 1)) * 100
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🎯 ATS Score", f"{score}%")

    with c2:
        st.metric("✅ Keywords Matched", len(matched))

    with c3:
        st.metric("❌ Missing Keywords", len(missing))

    st.progress(score / 100)

    # Resume Strength
    if score >= 80:
        st.success("🟢 Strong Match")

    elif score >= 60:
        st.warning("🟡 Moderate Match")

    else:
        st.error("🔴 Needs Improvement")

    st.divider()

    st.subheader("✅ Matched Keywords")

    for word in sorted(list(matched))[:30]:
        st.success(word)

    st.subheader("❌ Missing Keywords")

    for word in sorted(list(missing))[:30]:
        st.warning(word)

    st.success("ATS Analysis Completed Successfully 🚀")

