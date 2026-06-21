import streamlit as st

st.title("🛣️ AI Learning Roadmap")

current_skills = st.text_input(
    "Current Skills",
    "SQL, Excel"
)

target_role = st.selectbox(
    "Target Role",
    [
        "Data Analyst",
        "BI Analyst",
        "Data Engineer",
        "Data Scientist"
    ]
)

if st.button("Generate Roadmap"):

    roadmap = []

    if target_role == "Data Analyst":

        roadmap = [
            ("Month 1", "Advanced Excel"),
            ("Month 2", "SQL"),
            ("Month 3", "Power BI"),
            ("Month 4", "Python"),
            ("Month 5", "Projects"),
            ("Month 6", "Interview Preparation")
        ]

    elif target_role == "Data Engineer":

        roadmap = [
            ("Month 1", "Python"),
            ("Month 2", "Pandas"),
            ("Month 3", "Advanced SQL"),
            ("Month 4", "AWS"),
            ("Month 5", "ETL Concepts"),
            ("Month 6", "Projects")
        ]

    elif target_role == "Data Scientist":

        roadmap = [
            ("Month 1", "Python"),
            ("Month 2", "Pandas + NumPy"),
            ("Month 3", "Statistics"),
            ("Month 4", "Machine Learning"),
            ("Month 5", "Projects"),
            ("Month 6", "Model Deployment")
        ]

    elif target_role == "BI Analyst":

        roadmap = [
            ("Month 1", "Excel"),
            ("Month 2", "SQL"),
            ("Month 3", "Power BI"),
            ("Month 4", "DAX"),
            ("Month 5", "Dashboard Projects"),
            ("Month 6", "Interview Preparation")
        ]

    st.subheader("🚀 Your Learning Plan")

    for month, topic in roadmap:
        st.success(f"{month} → {topic}")

