
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

.stApp{
    background:
    radial-gradient(circle at top left,#1E1B4B 0%,#0B1120 40%),
    linear-gradient(135deg,#0B1120,#111827);
}

/* Metrics */
div[data-testid="metric-container"]{
    background:rgba(22,27,34,0.9);
    border:1px solid rgba(124,58,237,0.35);
    border-radius:20px;
    padding:20px;
    box-shadow:0px 0px 20px rgba(124,58,237,.15);
}

/* Buttons */
.stButton > button{
    height:70px;
    font-size:18px;
    font-weight:600;
    border-radius:18px;
    background:#161B22;
    border:1px solid rgba(255,255,255,.08);
}

.stButton > button:hover{
    border:1px solid #7C3AED;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

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
# LIVE DASHBOARD METRICS
# ==========================================================
st.markdown("""
<style>

.metric-card{
    background:rgba(22,27,34,0.85);
    border:1px solid rgba(124,58,237,.25);
    border-radius:22px;
    padding:25px;
    box-shadow:0px 0px 25px rgba(124,58,237,.15);
    transition:0.3s;
}

.metric-card:hover{
    transform:translateY(-4px);
    border:1px solid #7C3AED;
}

.metric-number{
    font-size:52px;
    font-weight:700;
    color:white;
}

.metric-label{
    color:#94A3B8;
    font-size:18px;
}

.metric-growth{
    color:#22C55E;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">

    💼 <span class="metric-label">Live Jobs</span>

    <div class="metric-number">
    {total_jobs}
    </div>

    <div class="metric-growth">
    ↗ Updated Live
    </div>

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">

    📄 <span class="metric-label">Resumes Analyzed</span>

    <div class="metric-number">
    {total_resumes}
    </div>

    <div class="metric-growth">
    ↗ +15%
    </div>

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">

    📈 <span class="metric-label">Skills Tracked</span>

    <div class="metric-number">
    {total_skills}
    </div>

    <div class="metric-growth">
    ↗ Live Market Data
    </div>

    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">

    💰 <span class="metric-label">Avg Salary</span>

    <div class="metric-number">
    ₹8.5
    </div>

    <div class="metric-growth">
    LPA
    </div>

    </div>
    """, unsafe_allow_html=True)

    
#------------------Job Intelligence----------    
st.subheader("💼 Job Intelligence")

j1, j2 = st.columns(2)

with j1:

    if st.button("🔍 Live Job Search", use_container_width=True):
        st.switch_page("pages/Search_Jobs.py")

    if st.button("🚀 Job Recommendation", use_container_width=True):
        st.switch_page("pages/Job_Recommendation.py")

with j2:

    if st.button("🏢 Company Analysis", use_container_width=True):
        st.switch_page("pages/Company_Analysis.py")

#------------------Resume Intelligence----------    
st.subheader("📄 Resume Intelligence")

r1, r2 = st.columns(2)

with r1:

    if st.button("📄 Resume Analyzer", use_container_width=True):
        st.switch_page("pages/Resume_Analyzer.py")

    if st.button("🎯 ATS Resume Score", use_container_width=True):
        st.switch_page("pages/ATS_Resume_Score.py")

    if st.button("✅ Resume Match Score", use_container_width=True):
        st.switch_page("pages/Resume_Match_Score.py")

with r2:

    if st.button("🤖 AI Resume Match", use_container_width=True):
        st.switch_page("pages/AI_Resume_Job_Match.py")
        
#------------------Skill Development----------    

st.subheader("📈 Skill Development")

s1, s2 = st.columns(2)

with s1:

    if st.button("⚡ Skill Gap Analyzer", use_container_width=True):
        st.switch_page("pages/Skill_Gap_Analyzer.py")

    if st.button("📊 Skills Analysis", use_container_width=True):
        st.switch_page("pages/Skills_Analysis.py")

with s2:

    if st.button("📚 Learning Roadmap", use_container_width=True):
        st.switch_page("pages/Learning_Roadmap.py")

#------------------Salary Intelligence----------    
st.subheader("💰 Salary Intelligence")

sal1, sal2 = st.columns(2)

with sal1:

    if st.button("💰 Salary Predictor", use_container_width=True):
        st.switch_page("pages/Salary_Predictor.py")

with sal2:

    if st.button("📈 Salary Insights", use_container_width=True):
        st.switch_page("pages/Salary_Insights.py")

# ---------------- Ai tools ----------------
st.subheader("🤖 AI Tools")

a1, a2 = st.columns(2)

with a1:

    if st.button("🤖 AI Career Advisor", use_container_width=True):
        st.switch_page("pages/AI_Career_Advisor.py")

with a2:

    if st.button("💬 AI Chatbot", use_container_width=True):
        st.switch_page("pages/AI_Chatbot.py")
# ==========================================================
# LIVE TRENDING SKILLS
# ==========================================================
import requests
from collections import Counter

st.divider()
st.subheader("🔥 Live Trending Skills")

skill_counter = Counter()

try:

    response = requests.get(
        "https://remoteok.com/api",
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    jobs = response.json()[1:]

    for job in jobs:

        tags = job.get("tags", [])

        for tag in tags:
            skill_counter[tag] += 1

except:
    st.warning("Unable to fetch live skills.")

# Top 10 skills
top_skills = skill_counter.most_common(10)

# Interactive search
search_skill = st.text_input(
    "🔍 Search Skill"
)

for skill, count in top_skills:

    if search_skill.lower() in skill.lower():

        percentage = min(count * 5, 100)

        st.progress(
            percentage / 100,
            text=f"{skill} ({count} jobs)"
        )

# ==========================================================
# SKILL TABLE
# ==========================================================
st.subheader("📊 Skill Demand Table")

import pandas as pd

skill_df = pd.DataFrame(
    top_skills,
    columns=["Skill", "Jobs Found"]
)

st.dataframe(
    skill_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# HOT SKILLS BADGES
# ==========================================================
st.subheader("🚀 Hottest Skills")

cols = st.columns(5)

for i, (skill, count) in enumerate(top_skills[:5]):

    with cols[i]:

        st.metric(
            skill,
            f"{count} Jobs"
        )

# ==========================================================
# FOOTER
# ==========================================================
st.divider()

st.caption(
    "🚀 SkillRadar AI | Career Intelligence Platform"
)


