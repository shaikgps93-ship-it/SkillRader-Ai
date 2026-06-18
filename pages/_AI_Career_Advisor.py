import streamlit as st

st.title("🤖 AI Career Advisor")

skills_input = st.text_area(
    "Enter your skills separated by commas",
    "SQL, Excel, Power BI"
)

if st.button("Get Career Advice"):

    skills = [skill.strip().lower()
              for skill in skills_input.split(",")]

    recommendations = []
    roles = []

    if "sql" in skills:
        recommendations.append("Learn Python")

    if "python" in skills:
        recommendations.append("Learn Pandas")

    if "pandas" in skills:
        recommendations.append("Learn AWS")

    if "power bi" in skills:
        roles.append("BI Analyst")

    if "excel" in skills:
        roles.append("Business Analyst")

    if "python" in skills and "sql" in skills:
        roles.append("Data Analyst")

    if "python" in skills and "aws" in skills:
        roles.append("Data Engineer")

    st.write("## 📚 Recommended Skills")

    for item in recommendations:
        st.success(item)

    st.write("## 💼 Suitable Roles")

    for role in roles:
        st.info(role)