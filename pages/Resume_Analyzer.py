import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader

st.title("📄 Resume Analyzer")

# Load jobs dataset
df = pd.read_csv("jobs.csv")

# Build market skill list
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

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        resume_text += page.extract_text()

    st.write("### Resume Text Preview")
    st.text(resume_text[:1000])

    found_skills = []

    for skill in market_skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    st.write("## Skills Found")
    st.success(", ".join(found_skills))

    missing_skills = market_skills - set(found_skills)

    st.write("## Missing Skills")

    for skill in missing_skills:
        st.warning(skill)
