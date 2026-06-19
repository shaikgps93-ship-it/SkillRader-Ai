import streamlit as st

st.set_page_config(
    page_title="AI Learning Roadmap",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Learning Roadmap")
st.caption("Choose a career path and get a complete roadmap.")

career_paths = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "AI Engineer",
    "Business Analyst",
    "Software Engineer",
    "Full Stack Developer",
    "QA Automation Engineer",
    "DevOps Engineer",
    "Cloud Engineer",
    "Cybersecurity Analyst",
    "Android Developer",
    "Game Developer",
    "Product Manager"
]

selected_role = st.selectbox(
    "🎯 Choose Career Path",
    career_paths
)

# ---------------- DATA ANALYST ----------------

if selected_role == "Data Analyst":

    st.subheader("📊 Data Analyst Roadmap")

    roadmap = [
        "Excel",
        "SQL",
        "Power BI",
        "Python",
        "Statistics",
        "Projects",
        "Portfolio",
        "Interview Preparation"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🆓 Free Resources")

        st.markdown("""
- freeCodeCamp SQL
- Alex The Analyst
- Kaggle Learn
- Microsoft Learn
- YouTube
""")

    with col2:

        st.subheader("🛠 Beginner Projects")

        st.markdown("""
- Sales Dashboard
- HR Analytics Dashboard
- Netflix Data Analysis
- Employee Attrition Analysis
""")
# ---------------- DATA SCIENTIST ----------------

if selected_role == "Data Scientist":

    st.subheader("🤖 Data Scientist Roadmap")

    roadmap = [
        "Python",
        "NumPy",
        "Pandas",
        "Statistics",
        "Data Visualization",
        "Machine Learning",
        "Deep Learning",
        "Projects",
        "Portfolio",
        "Interview Preparation"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🆓 Free Resources")

        st.markdown("""
- Kaggle Learn
- freeCodeCamp Python
- StatQuest YouTube
- Andrew Ng Machine Learning
- Microsoft Learn
""")

    with col2:

        st.subheader("🛠 Beginner Projects")

        st.markdown("""
- Titanic Survival Prediction
- House Price Prediction
- Customer Churn Prediction
- Iris Classification
""")

    st.divider()

    st.subheader("💰 Average Salary")

    st.info("₹10–20 LPA")

    st.subheader("📈 Career Progression")

    st.markdown("""
Data Scientist  
⬇  
Senior Data Scientist  
⬇  
Lead Data Scientist  
⬇  
AI Engineer
""")
