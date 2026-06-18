from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="🚀 SkillRadar AI",
    options=[
        "Dashboard",
        "Jobs",
        "Salary",
        "Resume",
        "AI Advisor"
    ],
    icons=[
        "grid",
        "search",
        "cash",
        "file-earmark-person",
        "robot"
    ],
    orientation="horizontal",
    styles={
        "container": {
            "background-color": "#141414"
        },
        "nav-link": {
            "color": "white",
            "font-size": "16px"
        },
        "nav-link-selected": {
            "background-color": "#E50914"
        }
    }
    import streamlit as st

if selected == "Dashboard":
    st.switch_page("pages/Dashboard.py")

elif selected == "Jobs":
    st.switch_page("pages/Search_Jobs.py")

elif selected == "Salary":
    st.switch_page("pages/Salary_Predictor.py")

elif selected == "Resume":
    st.switch_page("pages/_Resume_Analyzer.py")

elif selected == "AI Advisor":
    st.switch_page("pages/_AI_Career_Advisor.py")
)
