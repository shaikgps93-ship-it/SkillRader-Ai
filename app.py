import streamlit as st
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
)

if selected == "Dashboard":
    st.switch_page("pages/Dashboard.py")
