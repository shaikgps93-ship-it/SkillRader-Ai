import streamlit as st

st.title("🛣️ Learning Roadmap Generator")

skills_input = st.text_input(
    "Current Skills",
    "SQL, Excel"
)

target_role = st.selectbox(
    "Target Role",
    [
        "Data Analyst",
        "Data Engineer",
        "Data Scientist",
        "BI Analyst"
    ]
)

if st.button("Generate Roadmap"):

    skills = [
        skill.strip().lower()
        for skill in skills_input.split(",")
    ]

    roadmap = []

    if target_role == "Data Analyst":

        if "sql" not in skills:
            roadmap.append("Learn SQL")

        if "excel" not in skills:
            roadmap.append("Learn Excel")

        if "power bi" not in skills:
            roadmap.append("Learn Power BI")

        if "python" not in skills:
            roadmap.append("Learn Python")

    elif target_role == "Data Engineer":

        if "python" not in skills:
            roadmap.append("Learn Python")

        roadmap.append("Learn Pandas")
        roadmap.append("Learn Advanced SQL")
        roadmap.append("Learn AWS")
        roadmap.append("Learn ETL Concepts")

    elif target_role == "Data Scientist":

        roadmap.append("Learn Python")
        roadmap.append("Learn Pandas")
        roadmap.append("Learn NumPy")
        roadmap.append("Learn Machine Learning")
        roadmap.append("Build Projects")

    elif target_role == "BI Analyst":

        roadmap.append("Learn SQL")
        roadmap.append("Learn Power BI")
        roadmap.append("Learn DAX")
        roadmap.append("Create Dashboards")

    st.subheader("📚 Your Learning Roadmap")

    for i, step in enumerate(roadmap, start=1):
        st.success(f"Step {i}: {step}")