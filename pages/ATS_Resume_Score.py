import streamlit as st
from PyPDF2 import PdfReader

st.title("📄 ATS Resume Score")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if uploaded_file and job_description:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text()

    resume_text = resume_text.lower()
    jd_text = job_description.lower()

    jd_keywords = set(jd_text.split())
    resume_keywords = set(resume_text.split())

    matched = jd_keywords.intersection(resume_keywords)
    missing = jd_keywords - resume_keywords

    score = int((len(matched) / len(jd_keywords)) * 100)

    st.subheader("ATS Score")
    st.progress(score / 100)
    st.success(f"{score}/100")

    st.subheader("Matched Keywords")
    st.write(list(matched))

    st.subheader("Missing Keywords")
    st.write(list(missing))