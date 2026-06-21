
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0B1120,#111827);
}

div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #7C3AED;
    border-radius:15px;
    padding:15px;
}

.stButton > button{
    background:#7C3AED;
    color:white;
    border:none;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🤖 AI Career Advisor")
st.caption("Get personalized career guidance based on your skills")

# ---------------- INPUT ----------------
skills_input = st.text_input(
    "Enter Skills (comma separated)",
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

    # Skill Recommendations
    if "sql" in skills:
        recommended_skills.append("Python")

    if "python" in skills:
        recommended_skills.append("Pandas")

    if "pandas" in skills:
        recommended_skills.append("AWS")

    if "power bi" not in skills:
        recommended_skills.append("Power BI")

    # Future Roles
    if "sql" in skills and "excel" in skills:
        future_roles.append("Data Analyst")

    if "python" in skills and "sql" in skills:
        future_roles.append("BI Analyst")

    if "python" in skills and "aws" in skills:
        future_roles.append("Data Engineer")

    if "machine learning" in skills:
        future_roles.append("Data Scientist")

    # Salary Estimation
    if "python" in skills:
        salary_range = "7-10 LPA"

    if "aws" in skills:
        salary_range = "10-15 LPA"

    # Metrics
    c1, c2 = st.columns(2)

    with c1:
        st.metric("Expected Salary", salary_range)

    with c2:
        st.metric("Future Roles", len(future_roles))

    st.divider()

    # Recommended Skills
    st.subheader("📚 Recommended Skills")

    for skill in set(recommended_skills):
        st.info(skill)

    # Future Roles
    st.subheader("💼 Future Roles")

    for role in future_roles:
        st.success(role)

    # Learning Roadmap
    st.subheader("🚀 Learning Roadmap")

    roadmap = [
        "Learn Python",
        "Learn Pandas",
        "Build Projects",
        "Learn Advanced SQL",
        "Apply for Jobs"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.write(f"{i}. {step}")

    st.success("Career Advice Generated Successfully 🚀")
