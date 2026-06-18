import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- HIDE STREAMLIT UI ----------------
st.markdown("""
<style>

/* Hide sidebar */
[data-testid="stSidebar"] {
    display:none;
}

/* Hide sidebar toggle */
[data-testid="collapsedControl"] {
    display:none;
}

/* Hide Streamlit menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */
.stApp{
    background: linear-gradient(135deg,#0B1120,#111827);
    color:white;
}

/* Hero title */
.hero-title{
    font-size:65px;
    font-weight:bold;
    color:white;
}

.hero-sub{
    font-size:24px;
    color:#94A3B8;
}

/* Feature cards */
.card{
    background:#161B22;
    padding:25px;
    border-radius:20px;
    border:1px solid #2A2F3A;
    transition:0.3s;
}

.card:hover{
    border:1px solid #7C3AED;
}

.metric-box{
    background:#161B22;
    padding:20px;
    border-radius:18px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class='hero-title'>
AI-Powered Career <br>
<span style='color:#7C3AED'>Intelligence Platform</span>
</div>

<div class='hero-sub'>
Analyze • Learn • Grow • Get Hired
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- METRICS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Jobs Available", "12,540", "+8.2%")

with col2:
    st.metric("Skills Covered", "48+", "+5")

with col3:
    st.metric("Resumes Analyzed", "1,250", "+15%")

with col4:
    st.metric("Avg Salary", "₹8.5 LPA", "+7.4%")

st.divider()

# ---------------- FEATURES ----------------

st.subheader("🚀 Explore Features")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Search Jobs", use_container_width=True):
        st.switch_page("pages/Search_Jobs.py")

    if st.button("📄 Resume Analyzer", use_container_width=True):
        st.switch_page("pages/_Resume_Analyzer.py")

    if st.button("🎯 ATS Resume Score", use_container_width=True):
        st.switch_page("pages/ATS_Resume_Score.py")

with col2:
    if st.button("💰 Salary Predictor", use_container_width=True):
        st.switch_page("pages/Salary_Predictor.py")

    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

    if st.button("🧠 Skill Gap Analyzer", use_container_width=True):
        st.switch_page("pages/_Skill_Gap_Analyzer.py")

with col3:
    if st.button("🤖 AI Career Advisor", use_container_width=True):
        st.switch_page("pages/_AI_Career_Advisor.py")

    if st.button("📚 Learning Roadmap", use_container_width=True):
        st.switch_page("pages/Learning_Roadmap.py")

    if st.button("🏢 Company Analysis", use_container_width=True):
        st.switch_page("pages/_Company_Analysis.py")

st.divider()

# ---------------- SKILLS ----------------

st.subheader("Your Skills")

st.progress(90, text="Python")
st.progress(75, text="SQL")
st.progress(65, text="Power BI")
st.progress(55, text="Machine Learning")

# ---------------- FOOTER ----------------

st.write("")
st.caption("🚀 SkillRadar AI | Career Intelligence Platform")
