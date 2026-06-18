import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#0B1020;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background-color:#111827;
}

/* Metric cards */
div[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #00F5FF;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 0px 10px rgba(0,245,255,0.2);
}

/* Headers */
h1{
    color:#00F5FF;
}

h2,h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("""
# 🚀 SkillRadar AI

### Workforce Intelligence Platform

---
""")

# ---------------- HOME PAGE ----------------
st.title("🚀 SkillRadar AI")

st.subheader("AI-Powered Career Intelligence Platform")

st.write("Welcome to SkillRadar AI.")

st.markdown("""
### Available Modules

- 📊 Dashboard
- 🔥 Skills Analysis
- 💰 Salary Insights
- 🏢 Company Analysis
- 📄 Resume Analyzer
- 🤖 AI Career Advisor
- 📈 Salary Predictor
- 🔍 Search Jobs
- 🎯 Skill Gap Analyzer
""")

# ---------------- SAMPLE METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💼 Jobs", "8")

with col2:
    st.metric("🏢 Companies", "7")

with col3:
    st.metric("💰 Avg Salary", "9 LPA")

with col4:
    st.metric("🔥 Top Skill", "SQL")

st.divider()

st.success("SkillRadar AI is running successfully 🚀")

