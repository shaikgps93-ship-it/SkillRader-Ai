
import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Jobs",
    page_icon="🌍",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🌍 Live Job Search")
st.caption("Real-time jobs from RemoteOK")

search_term = st.text_input(
    "Search Skill or Role",
    "Python"
)

try:

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        "https://remoteok.com/api",
        headers=headers
    )

    jobs = response.json()[1:]

    job_list = []

    for job in jobs:

        role = job.get("position", "")
        company = job.get("company", "")
        location = job.get("location", "")
        tags = ", ".join(job.get("tags", []))

        if search_term.lower() in role.lower() or search_term.lower() in tags.lower():

            job_list.append({
                "Company": company,
                "Role": role,
                "Location": location,
                "Skills": tags
            })

    df = pd.DataFrame(job_list)

    st.metric(
        "Jobs Found",
        len(df)
    )

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error(
        f"Unable to load jobs: {e}"
    )

