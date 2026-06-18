
import streamlit as st
import requests
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Live Job Recommendation",
    page_icon="🚀",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("🚀 Live Job Recommendation Engine")
st.caption("Get job recommendations based on your skills")

# ---------------- USER INPUT ----------------
skills_input = st.text_input(
    "Enter Your Skills",
    "Python, SQL"
)

skills = [
    skill.strip().lower()
    for skill in skills_input.split(",")
]

job_list = []

# =====================================================
# REMOTEOK
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
        tags = [
            tag.lower()
            for tag in job.get("tags", [])
        ]
        url = job.get("url", "")

        # Match Score
        matches = len(
            set(skills).intersection(set(tags))
        )

        score = round(
            (matches / max(len(tags), 1)) * 100
        )

        if score > 0:

            job_list.append({
                "Company": company,
                "Role": role,
                "Location": location,
                "Match Score": score,
                "Apply Link": url
            })

except:
    st.warning("RemoteOK unavailable")

# =====================================================
# DISPLAY
# =====================================================
df = pd.DataFrame(job_list)

if len(df) > 0:

    df = df.sort_values(
        "Match Score",
        ascending=False
    )

    st.metric(
        "Recommended Jobs",
        len(df)
    )

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

    st.warning(
        "No matching jobs found."
    )

