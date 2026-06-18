
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

    # Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🚀 Jobs Found",
            len(df)
        )

    with c2:
        st.metric(
            "🏢 Companies",
            df["Company"].nunique()
        )

    with c3:
        st.metric(
            "🎯 Best Match",
            f"{df['Match Score'].max()}%"
        )

    st.divider()

    # Match Quality
    st.subheader("🎯 Match Quality")

    high = len(df[df["Match Score"] >= 80])
    medium = len(df[
        (df["Match Score"] >= 60) &
        (df["Match Score"] < 80)
    ])
    low = len(df[df["Match Score"] < 60])

    h1, h2, h3 = st.columns(3)

    with h1:
        st.success(f"🔥 High Match: {high}")

    with h2:
        st.warning(f"⚡ Medium Match: {medium}")

    with h3:
        st.error(f"📌 Low Match: {low}")

    st.divider()

    # Top Companies
    st.subheader("🏢 Top Companies Hiring")

    company_counts = (
        df["Company"]
        .value_counts()
        .head(5)
    )

    for company, count in company_counts.items():

        st.metric(
            company,
            f"{count} Jobs"
        )

    st.divider()

    # Career Paths
    st.subheader("🚀 Career Opportunities")

    st.progress(0.95, text="Data Analyst")
    st.progress(0.88, text="Business Analyst")
    st.progress(0.82, text="BI Analyst")
    st.progress(0.75, text="Data Engineer")

    st.divider()

    # Trending Skills
    st.subheader("🔥 Trending Skills")

    t1, t2, t3, t4 = st.columns(4)

    with t1:
        st.metric("Python", "High")

    with t2:
        st.metric("SQL", "High")

    with t3:
        st.metric("Power BI", "Growing")

    with t4:
        st.metric("AWS", "Very High")

    st.divider()

    # Job Table
    st.subheader("💼 Recommended Jobs")

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
