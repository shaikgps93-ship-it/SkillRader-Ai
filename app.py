import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SkillRadar AI",
    page_icon="🚀",
    layout="wide"
)

# Hide default sidebar navigation
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# Top Menu
selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Dashboard",
        "Jobs",
        "Salary",
        "Resume",
        "AI Advisor"
    ],
    icons=[
        "house",
        "bar-chart",
        "search",
        "currency-dollar",
        "file-earmark-text",
        "robot"
    ],
    orientation="horizontal"
)

# Page Content
if selected == "Home":
    st.title("🚀 SkillRadar AI")

elif selected == "Dashboard":
    st.switch_page("pages/Dashboard.py")

elif selected == "Jobs":
    st.switch_page("pages/Search_Jobs.py")

elif selected == "Salary":
    st.switch_page("pages/Salary_Predictor.py")

elif selected == "Resume":
    st.switch_page("pages/AI_Resume_Job_Match.py")

elif selected == "AI Advisor":
    st.switch_page("pages/AI_Career_Advisor.py")
