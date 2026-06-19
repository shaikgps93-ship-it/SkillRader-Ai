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
    # ---------------- DATA ENGINEER ----------------

if selected_role == "Data Engineer":

    st.subheader("🏗 Data Engineer Roadmap")

    roadmap = [
        "SQL",
        "Python",
        "Data Warehousing",
        "ETL Concepts",
        "Apache Spark",
        "Airflow",
        "AWS",
        "Snowflake",
        "Projects",
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
- AWS Skill Builder
- Databricks Academy
- Microsoft Learn
- YouTube
""")

    with col2:

        st.subheader("🛠 Projects")

        st.markdown("""
- ETL Pipeline
- Data Warehouse Project
- Spark Analytics
- AWS S3 Pipeline
""")

    st.info("💰 Average Salary: ₹12–25 LPA")

# ---------------- AI ENGINEER ----------------

if selected_role == "AI Engineer":

    st.subheader("🤖 AI Engineer Roadmap")

    roadmap = [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "Transformers",
        "LangChain",
        "RAG",
        "LLM Projects",
        "Deployment"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹15–35 LPA")

# ---------------- QA AUTOMATION ----------------

if selected_role == "QA Automation Engineer":

    st.subheader("🧪 QA Automation Engineer")

    roadmap = [
        "Manual Testing",
        "SQL",
        "Python",
        "Selenium",
        "API Testing",
        "Postman",
        "JMeter",
        "CI/CD"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹8–18 LPA")


# ---------------- DEVOPS ----------------

if selected_role == "DevOps Engineer":

    st.subheader("☁ DevOps Engineer")

    roadmap = [
        "Linux",
        "Git",
        "Docker",
        "Kubernetes",
        "Jenkins",
        "AWS",
        "Terraform",
        "Monitoring"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹12–30 LPA")
    # ---------------- SOFTWARE ENGINEER ----------------

if selected_role == "Software Engineer":

    st.subheader("💻 Software Engineer Roadmap")

    roadmap = [
        "Programming Fundamentals",
        "Python / Java",
        "OOP",
        "Data Structures & Algorithms",
        "Git & GitHub",
        "APIs",
        "Databases",
        "Projects",
        "Interview Preparation"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹8–25 LPA")

# ---------------- FULL STACK ----------------

if selected_role == "Full Stack Developer":

    st.subheader("🌐 Full Stack Developer Roadmap")

    roadmap = [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Express",
        "MongoDB",
        "REST APIs",
        "Deployment"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹8–22 LPA")
    # ---------------- BUSINESS ANALYST ----------------

if selected_role == "Business Analyst":

    st.subheader("📊 Business Analyst Roadmap")

    roadmap = [
        "Excel",
        "SQL",
        "Power BI",
        "Requirement Gathering",
        "Agile Methodology",
        "Jira",
        "Stakeholder Management",
        "Projects"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹7–18 LPA")

# ---------------- CYBERSECURITY ----------------

if selected_role == "Cybersecurity Analyst":

    st.subheader("🛡 Cybersecurity Analyst Roadmap")

    roadmap = [
        "Networking",
        "Linux",
        "Python",
        "Security Fundamentals",
        "SIEM Tools",
        "SOC Concepts",
        "Ethical Hacking Basics",
        "Projects"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹8–20 LPA")
    

# ---------------- ANDROID ----------------

if selected_role == "Android Developer":

    st.subheader("📱 Android Developer Roadmap")

    roadmap = [
        "Java / Kotlin",
        "Android Studio",
        "Layouts",
        "Firebase",
        "REST APIs",
        "Projects",
        "Play Store Deployment"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹7–18 LPA")

# ---------------- GAME DEVELOPMENT ----------------

if selected_role == "Game Developer":

    st.subheader("🎮 Game Developer Roadmap")

    roadmap = [
        "C#",
        "Unity",
        "Game Physics",
        "Animations",
        "AI for Games",
        "Blender Basics",
        "Publishing"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹7–20 LPA")
    # ---------------- PRODUCT MANAGER ----------------

if selected_role == "Product Manager":

    st.subheader("📦 Product Manager Roadmap")

    roadmap = [
        "Business Fundamentals",
        "Agile",
        "Jira",
        "Analytics",
        "User Research",
        "Stakeholder Management",
        "Roadmap Planning"
    ]

    for i, step in enumerate(roadmap, start=1):
        st.success(f"{i}. {step}")

    st.info("💰 Average Salary: ₹12–30 LPA")
    
