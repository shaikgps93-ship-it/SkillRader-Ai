from utils.navigation import home_button

home_button()

import streamlit as st

st.title("🤖 AI Career Advisor")

st.write("Get personalized career guidance based on your current skills.")

# User input
skills_input = st.text_input(
    "Enter your skills (comma separated)",
    "SQL, Excel, Power BI"
)

if st.button("Generate Advice"):

    skills = [
        skill.strip().lower()
        for skill in skills_input.split(",")
    ]

    recommended_skills = []
    future_roles = []
    salary_range = "5-7 LPA"

    # Recommendations
    if "sql" in skills:
        recommended_skills.append("Python")

    if "python" in skills:
        recommended_skills.append("Pandas")

    if "pandas" in skills:
        recommended_skills.append("AWS")

    if "power bi" not in skills:
        recommended_skills.append("Power BI")

    # Roles
    if "sql" in skills and "excel" in skills:
        future_roles.append("Data Analyst")

    if "python" in skills and "sql" in skills:
        future_roles.append("BI Analyst")

    if "python" in skills and "aws" in skills:
        future_roles.append("Data Engineer")

    if "python" in skills and "machine learning" in skills:
        future_roles.append("Data Scientist")

    # Salary estimation
    if "python" in skills:
        salary_range = "7-10 LPA"

    if "aws" in skills:
        salary_range = "10-15 LPA"

    # Display
    st.subheader("🎯 Career Advice")

    st.success(f"Expected Salary: {salary_range}")

    st.subheader("📚 Recommended Next Skills")

    for skill in set(recommended_skills):
        st.info(skill)

    st.subheader("💼 Future Roles")

    for role in future_roles:
        st.success(role)

    st.subheader("🚀 Learning Roadmap")

    roadmap = [
        "Learn Python",
        "Learn Pandas",
        "Build Projects",
        "Learn SQL Advanced",
        "Apply for Jobs"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.write(f"{i}. {step}")

