
import streamlit as st
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0B1120,#111827);
}

div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #7C3AED;
    border-radius:15px;
    padding:15px;
}

.stButton > button{
    background:#7C3AED;
    color:white;
    border:none;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("💰 AI Salary Predictor")
st.caption("Estimate your market salary based on experience")

# ---------------- LOAD DATA ----------------
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ---------------- CLEAN DATA ----------------
df["salary_value"] = (
    df["salary"]
    .str.replace(" LPA", "", regex=False)
    .astype(float)
)

df["experience_value"] = (
    df["experience"]
    .str.replace(" Years", "", regex=False)
    .str.replace(" Year", "", regex=False)
    .astype(int)
)

# ---------------- MODEL ----------------
X = df[["experience_value"]]
y = df["salary_value"]

model = LinearRegression()
model.fit(X, y)

# ---------------- USER INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    experience = st.slider(
        "📈 Years of Experience",
        1,
        10,
        2
    )

with col2:
    skills = st.multiselect(
        "🛠 Skills",
        ["SQL", "Python", "Power BI", "AWS", "Excel"]
    )

# ---------------- PREDICTION ----------------
prediction = model.predict([[experience]])

st.divider()

st.metric(
    "Predicted Salary",
    f"₹ {prediction[0]:.2f} LPA"
)

# ---------------- GAUGE ----------------
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prediction[0],
    title={"text": "Salary Prediction"},
    gauge={
        "axis": {"range": [0, 20]}
    }
))

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- RECOMMENDATIONS ----------------
st.subheader("🚀 Recommendations")

if "SQL" in skills and "Python" not in skills:
    st.info("Learn Python to increase salary potential.")

if "Python" in skills and "AWS" not in skills:
    st.info("Learn AWS for Data Engineering roles.")

if "Excel" in skills and "Power BI" not in skills:
    st.info("Learn Power BI for BI Analyst roles.")

st.success("Salary Prediction Complete 🚀")

