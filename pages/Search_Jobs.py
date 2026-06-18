
import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Job Search",
    page_icon="🌍",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8, 1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🌍 Live Job Search")
st.caption("Real-time jobs from RemoteOK")

# ---------------- SEARCH ----------------
search_term = st.text_input(
    "Search Skill or Role",
    "analyst"
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
        url = job.get("url", "")

        if (
            search_term.lower() in role.lower()
            or search_term.lower() in tags.lower()
        ):

            job_list.append({
                "Company": company,
                "Role": role,
                "Location": location,
                "Skills": tags,
                "Apply Link": url
            })

    df = pd.DataFrame(job_list)

    # Remove 0,1,2 index column
    df.reset_index(drop=True, inplace=True)

    st.metric(
        "Jobs Found",
        len(df)
    )

    st.data_editor(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Apply Link": st.column_config.LinkColumn(
                "Apply Now 🔗",
                display_text="Apply"
            )
        }
    )

except Exception as e:

    st.error(
        f"Unable to load jobs: {e}"
    )

