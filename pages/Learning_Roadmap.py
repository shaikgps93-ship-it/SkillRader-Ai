
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📚",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("📚 AI Learning Roadmap")
st.caption("Personalized roadmap with free learning resources")

career = st.selectbox(
    "Choose Career Path",
    [
        "Data Analyst",
        "Data Engineer",
        "Data Scientist"
    ]
)

# ==================================================
# DATA ANALYST
# ==================================================
if career == "Data Analyst":

    roadmap = [
        ("Month 1", "Excel",
         "Excel skills are essential for reporting and analysis.",
         "https://youtube.com/playlist?list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF"),

        ("Month 2", "SQL",
         "Learn SQL joins, group by and window functions.",
         "https://www.w3schools.com/sql/"),

        ("Month 3", "Power BI",
         "Build dashboards and reports.",
         "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"),

        ("Month 4", "Python",
         "Learn Pandas and NumPy.",
         "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"),

        ("Month 5", "Projects",
         "Create portfolio projects and upload to GitHub.",
         "https://www.kaggle.com/"),

        ("Month 6", "Interview Preparation",
         "Practice SQL and Python questions.",
         "https://www.hackerrank.com/domains/sql")
    ]


# ==================================================
# DATA ENGINEER
# ==================================================
elif career == "Data Engineer":

    roadmap = [
        ("Month 1", "Python",
         "Learn core Python concepts.",
         "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"),

        ("Month 2", "SQL",
         "Master advanced SQL.",
         "https://www.w3schools.com/sql/"),

        ("Month 3", "Pandas",
         "Learn data manipulation.",
         "https://pandas.pydata.org/docs/getting_started/index.html"),

        ("Month 4", "AWS",
         "Learn cloud basics.",
         "https://aws.amazon.com/training/digital/"),

        ("Month 5", "ETL Concepts",
         "Understand pipelines and workflows.",
         "https://airflow.apache.org/docs/"),

        ("Month 6", "Spark",
         "Learn big data processing.",
         "https://spark.apache.org/docs/latest/")
    ]


# ==================================================
# DATA SCIENTIST
# ==================================================
else:

    roadmap = [
        ("Month 1", "Python",
         "Build a strong foundation.",
         "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"),

        ("Month 2", "Pandas + NumPy",
         "Data analysis fundamentals.",
         "https://pandas.pydata.org/docs/getting_started/index.html"),

        ("Month 3", "Statistics",
         "Learn probability and statistics.",
         "https://www.khanacademy.org/math/statistics-probability"),

        ("Month 4", "Machine Learning",
         "Study supervised and unsupervised learning.",
         "https://developers.google.com/machine-learning/crash-course"),

        ("Month 5", "Deep Learning",
         "Learn neural networks.",
         "https://www.deeplearning.ai/"),

        ("Month 6", "Projects",
         "Build Kaggle projects.",
         "https://www.kaggle.com/")
    ]

# ==================================================
# DISPLAY ROADMAP
# ==================================================
st.divider()

for month, topic, suggestion, resource in roadmap:

    with st.container(border=True):

        st.subheader(f"✅ {month}")
        st.write(f"### {topic}")

        st.info(f"💡 Suggestion: {suggestion}")

        st.link_button(
            "📖 Free Resource",
            resource
        )

st.success("Roadmap Generated Successfully 🚀")

