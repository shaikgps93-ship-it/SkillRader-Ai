
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
# ---------------- SKILLS ----------------
st.subheader("Top Skills")

st.progress(90, text="Python")
st.progress(80, text="SQL")
st.progress(70, text="Power BI")
st.progress(60, text="Machine Learning")

# ---------------- FOOTER ----------------
st.write("")
st.caption("🚀 SkillRadar AI | Career Intelligence Platform")

