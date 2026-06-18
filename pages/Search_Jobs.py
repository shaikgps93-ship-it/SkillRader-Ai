
import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Multi-Portal Jobs",
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
st.caption("Jobs from RemoteOK + Arbeitnow + Remotive")

search_term = st.text_input(
    "Search Role or Skill",
    "Data Analyst"
)

job_list = []

# =====================================================
# RemoteOK
# =====================================================
try:

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        "https://remoteok.com/api",
        headers=headers
    )

    jobs = response.json()[1:]

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
                "Source": "RemoteOK",
                "Company": company,
                "Role": role,
                "Location": location,
                "Skills": tags,
                "Apply Link": url
            })

except:
    pass


# =====================================================
# Arbeitnow
# =====================================================
try:

    response = requests.get(
        "https://www.arbeitnow.com/api/job-board-api"
    )

    jobs = response.json()["data"]

    for job in jobs:

        role = job.get("title", "")
        company = job.get("company_name", "")
        location = job.get("location", "")
        tags = ", ".join(job.get("tags", []))
        url = job.get("url", "")

        if (
            search_term.lower() in role.lower()
            or search_term.lower() in tags.lower()
        ):

            job_list.append({
                "Source": "Arbeitnow",
                "Company": company,
                "Role": role,
                "Location": location,
                "Skills": tags,
                "Apply Link": url
            })

except:
    pass


# =====================================================
# Remotive
# =====================================================
try:

    response = requests.get(
        "https://remotive.com/api/remote-jobs"
    )

    jobs = response.json()["jobs"]

    for job in jobs:

        role = job.get("title", "")
        company = job.get("company_name", "")
        location = job.get("candidate_required_location", "")
        tags = ", ".join(job.get("tags", []))
        url = job.get("url", "")

        if (
            search_term.lower() in role.lower()
            or search_term.lower() in tags.lower()
        ):

            job_list.append({
                "Source": "Remotive",
                "Company": company,
                "Role": role,
                "Location": location,
                "Skills": tags,
                "Apply Link": url
            })

except:
    pass


# =====================================================
# DISPLAY
# =====================================================

df = pd.DataFrame(job_list)

df.reset_index(drop=True, inplace=True)

st.metric(
    "Jobs Found",
    len(df)
)

if len(df) > 0:

    st.data_editor(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Apply Link": st.column_config.LinkColumn(
                "Apply 🚀",
                display_text="Apply"
            )
        }
    )

else:

    st.warning("No jobs found.")

