```python
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0B1120,#111827);
}

h1,h2,h3{
    color:white;
}

div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #7C3AED;
    border-radius:18px;
    padding:15px;
}

.stButton > button{
    background:#7C3AED;
    color:white;
    border:none;
    border-radius:12px;
}

.stButton > button:hover{
    background:#9333EA;
}

</style>
""", unsafe_allow_html=True)

# Home Button
col1, col2 = st.columns([8,1])

with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# Header
st.markdown("""
<h1>📊 Dashboard</h1>
<p style='color:#94A3B8'>
Workforce Analytics Overview
</p>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Jobs Available", "12,540", "+8%")

with col2:
    st.metric("Skills Covered", "48+", "+5")

with col3:
    st.metric("Resumes Analyzed", "1,250", "+15%")

with col4:
    st.metric("Average Salary", "₹8.5 LPA", "+7%")

st.divider()

# Skills Progress
st.subheader("Top Skills")

st.progress(90, text="Python")
st.progress(80, text="SQL")
st.progress(70, text="Power BI")
st.progress(60, text="Machine Learning")

st.divider()

st.success("Dashboard Loaded Successfully 🚀")
```
