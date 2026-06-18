
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📚",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8, 1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("📚 AI Learning Roadmap")
st.caption("Personalized roadmap with free resources and projects")

career = st.selectbox(
    "Choose Career Path",
    [
        "Data Analyst",
        "Data Engineer",
        "Data Scientist"
    ]
)

# ==========================================================
# DATA ANALYST
# ==========================================================
if career == "Data Analyst":

    roadmap = [

        (
            "Month 1",
            "Excel",
            "Learn formulas, pivot tables and charts.",
            "Build a Sales Dashboard in Excel",
            "https://youtube.com/playlist?list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF"
        ),

        (
            "Month 2",
            "SQL",
            "Master joins, group by and window functions.",
            "Employee Database Analysis Project",
            "https://www.w3schools.com/sql/"
        ),

        (
            "Month 3",
            "Power BI",
            "Create dashboards and reports.",
            "HR Analytics Dashboard",
            "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"
        ),

        (
            "Month 4",
            "Python",
            "Learn Pandas and NumPy.",
            "Netflix Data Analysis Project",
            "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
        ),

        (
            "Month 5",
            "Projects",
            "Build portfolio projects.",
            "End-to-End Data Analyst Portfolio",
            "https://www.kaggle.com/"
        ),

        (
            "Month 6",
            "Interview Preparation",
            "Practice SQL and Python questions.",
            "Mock Interview + Resume Optimization",
            "https://www.hackerrank.com/domains/sql"
        )
    ]

    capstone = """
### 🎓 Final Capstone Project

Employee Attrition Analysis

Tools Used:
- Excel
- SQL
- Power BI
- Python

Deliverables:
✅ Dashboard
✅ Insights Report
✅ GitHub Project
✅ Resume Project Section
"""

# ==========================================================
# DATA ENGINEER
# ==========================================================
elif career == "Data Engineer":

    roadmap = [

        (
            "Month 1",
            "Python",
            "Learn core Python concepts.",
            "Python Automation Project",
            "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
        ),

        (
            "Month 2",
            "SQL",
            "Master advanced SQL.",
            "Database Analytics Project",
            "https://www.w3schools.com/sql/"
        ),

        (
            "Month 3",
            "Pandas",
            "Learn data manipulation.",
            "CSV Cleaning Project",
            "https://pandas.pydata.org/docs/getting_started/index.html"
        ),

        (
            "Month 4",
            "AWS",
            "Learn cloud fundamentals.",
            "Deploy a Sample App on AWS",
            "https://aws.amazon.com/training/digital/"
        ),

        (
            "Month 5",
            "ETL Concepts",
            "Understand pipelines and workflows.",
            "ETL Pipeline Project",
            "https://airflow.apache.org/docs/"
        ),

        (
            "Month 6",
            "Spark",
            "Learn big data processing.",
            "PySpark Data Processing Project",
            "https://spark.apache.org/docs/latest/"
        )
    ]

    capstone = """
### 🎓 Final Capstone Project

End-to-End Data Pipeline

Tools Used:
- Python
- SQL
- AWS
- Spark

Deliverables:
✅ ETL Pipeline
✅ Cloud Deployment
✅ GitHub Repository
"""

# ==========================================================
# DATA SCIENTIST
# ==========================================================
else:

    roadmap = [

        (
            "Month 1",
            "Python",
            "Build a strong foundation.",
            "Python Mini Projects",
            "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
        ),

        (
            "Month 2",
            "Pandas + NumPy",
            "Data analysis fundamentals.",
            "Netflix Dataset Analysis",
            "https://pandas.pydata.org/docs/getting_started/index.html"
        ),

        (
            "Month 3",
            "Statistics",
            "Understand probability and statistics.",
            "Statistics Case Study",
            "https://www.khanacademy.org/math/statistics-probability"
        ),

        (
            "Month 4",
            "Machine Learning",
            "Learn supervised learning.",
            "House Price Prediction Project",
            "https://developers.google.com/machine-learning/crash-course"
        ),

        (
            "Month 5",
            "Deep Learning",
            "Learn neural networks.",
            "Image Classification Project",
            "https://www.deeplearning.ai/"
        ),

        (
            "Month 6",
            "Projects",
            "Build portfolio projects.",
            "Kaggle Competition Project",
            "https://www.kaggle.com/"
        )
    ]

    capstone = """
### 🎓 Final Capstone Project

Customer Churn Prediction System

Tools Used:
- Python
- Pandas
- Scikit-Learn

Deliverables:
✅ Machine Learning Model
✅ Dashboard
✅ GitHub Repository
"""

# ==========================================================
# DISPLAY ROADMAP
# ==========================================================

st.divider()

for month, topic, suggestion, project, resource in roadmap:

    with st.container(border=True):

        st.subheader(f"✅ {month}")
        st.write(f"### {topic}")

        st.info(f"💡 Suggestion: {suggestion}")

        st.success(f"🚀 Project: {project}")

        st.link_button(
            "📖 Free Resource",
            resource
        )

st.divider()

st.markdown(capstone)

st.success("Roadmap Generated Successfully 🚀")

