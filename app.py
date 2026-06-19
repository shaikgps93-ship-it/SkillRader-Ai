
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Hide Streamlit UI */
[data-testid="stSidebar"] {
    display:none;
}

[data-testid="collapsedControl"] {
    display:none;
}

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    visibility:hidden;
}

/* Background */
.stApp{
    background: linear-gradient(135deg,#0B1120,#111827);
    color:white;
}

/* Hero */
.hero-title{
    font-size:65px;
    font-weight:bold;
    color:white;
}

.hero-sub{
    font-size:24px;
    color:#94A3B8;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div style="text-align:center;padding-top:25px;">

<h1 style="
font-size:80px;
font-weight:800;
margin-bottom:0;
color:white;">
🚀 SkillRadar AI
</h1>

<h2 style="
color:#7C3AED;
font-weight:600;
margin-top:10px;">
AI Career Intelligence Platform
</h2>

<p style="
font-size:22px;
color:#94A3B8;
margin-top:20px;">
Analyze • Learn • Grow • Get Hired
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
# ==========================================================
# LIVE METRICS
# ==========================================================
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "💼 Live Jobs",
        "12,540",
        "+8%"
    )

with m2:
    st.metric(
        "📄 Resumes Analyzed",
        "1,250+",
        "+15%"
    )

with m3:
    st.metric(
        "📈 Skills Tracked",
        "500+",
        "+12%"
    )

with m4:
    st.metric(
        "💰 Avg Salary",
        "₹8.5 LPA",
        "+7%"
    )

st.divider()


# ---------------- METRICS ----------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Jobs Available", "12,540")

with m2:
    st.metric("Skills Covered", "48+")

with m3:
    st.metric("Resumes Analyzed", "1,250")

with m4:
    st.metric("Avg Salary", "₹8.5 LPA")

st.divider()

# ---------------- FEATURES ----------------
st.subheader("🚀 Explore Features")

col1, col2, col3 = st.columns(3)

# ---------------- COLUMN 1 ----------------
with col1:

    if st.button("🔍 Live Job Search", use_container_width=True):
        st.switch_page("pages/Search_Jobs.py")

    if st.button("📄 Resume Analyzer", use_container_width=True):
        st.switch_page("pages/Resume_Analyzer.py")

    if st.button("🎯 ATS Resume Score", use_container_width=True):
        st.switch_page("pages/ATS_Resume_Score.py")

    if st.button("✅ Resume Match Score", use_container_width=True):
        st.switch_page("pages/Resume_Match_Score.py")

    if st.button("🤖 AI Resume Match", use_container_width=True):
        st.switch_page("pages/AI_Resume_Job_Match.py")


# ---------------- COLUMN 2 ----------------
with col2:

    if st.button("💰 Salary Predictor", use_container_width=True):
        st.switch_page("pages/Salary_Predictor.py")

    if st.button("💹 Salary Insights", use_container_width=True):
        st.switch_page("pages/Salary_Insights.py")

    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

    if st.button("⚡ Skill Gap Analyzer", use_container_width=True):
        st.switch_page("pages/Skill_Gap_Analyzer.py")

    if st.button("📈 Skills Analysis", use_container_width=True):
        st.switch_page("pages/Skills_Analysis.py")


# ---------------- COLUMN 3 ----------------
with col3:

    if st.button("🤖 AI Career Advisor", use_container_width=True):
        st.switch_page("pages/AI_Career_Advisor.py")

    if st.button("🤖 AI Chatbot", use_container_width=True):
        st.switch_page("pages/AI_Chatbot.py")

    if st.button("📚 Learning Roadmap", use_container_width=True):
        st.switch_page("pages/Learning_Roadmap.py")

    if st.button("🏢 Company Analysis", use_container_width=True):
        st.switch_page("pages/Company_Analysis.py")

    if st.button("🚀 Job Recommendation", use_container_width=True):
        st.switch_page("pages/Job_Recommendation.py")

st.divider()

# ---------------- SKILLS ----------------
st.subheader("Top Skills")

st.progress(90, text="Python")
st.progress(80, text="SQL")
st.progress(70, text="Power BI")
st.progress(60, text="Machine Learning")

# ---------------- FOOTER ----------------
st.write("")
st.caption("🚀 SkillRadar AI | Career Intelligence Platform")

