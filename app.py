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
.stApp {
    background-color: #0E1117;
    color: white;
}

.main-title {
    font-size: 55px;
    font-weight: bold;
    color: #00E5FF;
}

.sub-title {
    font-size: 28px;
    color: #A0AEC0;
}

.feature-card {
    background: #1A1D24;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2D3748;
    margin-bottom: 15px;
}

.metric-box {
    background: #1A1D24;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>🚀 SkillRadar AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI-Powered Career Intelligence Platform</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Modules", "8")

with col2:
    st.metric("AI Tools", "6")

with col3:
    st.metric("Jobs Indexed", "100+")

with col4:
    st.metric("Career Insights", "24/7")

st.divider()

# ---------------- FEATURES ----------------
st.subheader("⚡ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-card'>
    🔍 Search Jobs<br><br>
    Find opportunities from your database.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    💰 Salary Predictor<br><br>
    Predict salaries using AI.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    📄 Resume Analyzer<br><br>
    Match resumes with job descriptions.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
    📊 Dashboard<br><br>
    Workforce analytics and insights.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    🧠 Skill Analysis<br><br>
    Discover missing skills and recommendations.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    🤖 AI Career Advisor<br><br>
    Personalized career guidance.
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.success("✅ Use the sidebar to navigate between pages.")
