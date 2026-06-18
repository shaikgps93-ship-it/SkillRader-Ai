
import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0B1120, #111827);
}

div[data-testid="metric-container"] {
    background: #161B22;
    border: 1px solid #7C3AED;
    border-radius: 15px;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

# Home button
col1, col2 = st.columns([8,1])

with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# Header
st.title("📊 Dashboard")
st.caption("Workforce Analytics Overview")

# Metrics
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Jobs", "12,540")

with c2:
    st.metric("Skills", "48+")

with c3:
    st.metric("Resumes", "1,250")

with c4:
    st.metric("Avg Salary", "₹8.5 LPA")

st.divider()

st.subheader("Top Skills")

st.progress(90, text="Python")
st.progress(80, text="SQL")
st.progress(70, text="Power BI")
st.progress(60, text="Machine Learning")

st.success("Dashboard Loaded Successfully 🚀")

