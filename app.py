import streamlit as st

st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("🚀 SkillRadar AI")
st.sidebar.caption("Career Intelligence Platform")

st.title("🚀 SkillRadar AI")
st.subheader("AI-Powered Career Intelligence Platform")

st.markdown("""
Find jobs • Analyze resumes • Predict salaries • Close skill gaps
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Total Modules", 12)

with col2:
    st.metric("🤖 AI Features", 6)

with col3:
    st.metric("☁️ Deployment", "Live")

st.markdown("---")

st.info("📄 Resume Analyzer")
st.info("💰 Salary Predictor")
st.info("🎯 Skill Gap Analyzer")
st.info("🤖 AI Career Advisor")
st.info("🔍 Job Search Engine")
