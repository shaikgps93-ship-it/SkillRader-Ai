import streamlit as st

st.title("🤖 SkillRadar AI Assistant")

question = st.text_input(
    "Ask me anything...",
    placeholder="What should I learn after SQL?"
)

if question:

    q = question.lower()

    if "sql" in q:
        response = """
Learn Python next.

Roadmap:
1. SQL
2. Python
3. Pandas
4. Power BI
5. Projects
"""
    elif "salary" in q:
        response = """
Average Data Analyst salary:
₹5–10 LPA

Data Engineer:
₹8–15 LPA
"""
    elif "python" in q:
        response = """
After Python, learn:
• Pandas
• NumPy
• Machine Learning
"""
    elif "power bi" in q:
        response = """
Power BI + SQL is excellent for Data Analyst roles.
"""
    else:
        response = """
I recommend:

• SQL
• Python
• Pandas
• Power BI
• Projects
"""

    st.success(response)
