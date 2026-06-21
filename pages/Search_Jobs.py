import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Live Job Search",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Live Job Search")
st.caption("Real-time jobs from multiple job portals")

search_term = st.text_input(
    "Search Skill or Role",
    "Data Analyst"
)

jobs = []

# ================= RemoteOK =================
try:
    response = requests.get(
        "https://remoteok.com/api",
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    data = response.json()[1:]

    for job in data:

        title = job.get("position", "")
        company = job.get("company", "")
        location = job.get("location", "")
        tags = ", ".join(job.get("tags", []))
        url = job.get("url", "")

        if search_term.lower() in title.lower():

            jobs.append({
                "Company": company,
                "Role": title,
                "Location": location,
                "Skills": tags,
                "Apply": url
            })

except:
    st.warning("RemoteOK unavailable")


# ================= Remotive =================
try:
    response = requests.get(
        "https://remotive.com/api/remote-jobs",
        timeout=10
    )

    data = response.json()["jobs"]

    for job in data:

        title = job["title"]

        if search_term.lower() in title.lower():

            jobs.append({
                "Company": job["company_name"],
                "Role": title,
                "Location": job["candidate_required_location"],
                "Skills": ", ".join(job.get("tags", [])),
                "Apply": job["url"]
            })

except:
    st.warning("Remotive unavailable")


# ================= ArbeitNow =================
try:
    response = requests.get(
        "https://www.arbeitnow.com/api/job-board-api",
        timeout=10
    )

    data = response.json()["data"]

    for job in data:

        title = job["title"]

        if search_term.lower() in title.lower():

            jobs.append({
                "Company": job["company_name"],
                "Role": title,
                "Location": job["location"],
                "Skills": ", ".join(job.get("tags", [])),
                "Apply": job["url"]
            })

except:
    st.warning("ArbeitNow unavailable")


# ================= DISPLAY =================
df = pd.DataFrame(jobs)

if len(df) > 0:

    st.subheader(f"Jobs Found: {len(df)}")

    st.data_editor(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Apply": st.column_config.LinkColumn(
                "Apply 🚀",
                display_text="Open"
            )
        }
    )

else:

    st.error("No jobs found.")
