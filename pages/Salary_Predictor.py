
import streamlit as st
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="AI Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# ==========================================================
# PREMIUM CSS
# ==========================================================
st.markdown("""
<style>

/* Background */
.stApp{
    background:
    radial-gradient(circle at top left,#1E1B4B 0%,#0B1120 45%),
    linear-gradient(135deg,#0B1120,#111827);
    color:white;
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:rgba(22,27,34,0.9);
    border:1px solid rgba(124,58,237,0.4);
    border-radius:20px;
    padding:18px;
    box-shadow:0px 0px 20px rgba(124,58,237,0.15);
}

/* Buttons */
.stButton > button{
    background:linear-gradient(90deg,#7C3AED,#9333EA);
    color:white;
    border:none;
    border-radius:15px;
}

/* Glass Card */
.glass-card{
    background:rgba(22,27,34,0.75);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HOME BUTTON
# ==========================================================
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
# 💰 AI Salary Predictor

Discover your earning potential with AI.
""")

# ==========================================================
# LOAD DATABASE
# ==========================================================
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ==========================================================
# CLEAN DATA
# ==========================================================
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

# ==========================================================
# MODEL
# ==========================================================
X = df[["experience_value"]]
y = df["salary_value"]

model = LinearRegression()
model.fit(X, y)

# ==========================================================
# USER INPUT
# ==========================================================
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
        [
            "SQL",
            "Python",
            "Power BI",
            "AWS",
            "Excel",
            "Spark",
            "Docker"
        ]
    )

# ==========================================================
# PREDICTION
# ==========================================================
prediction = model.predict([[experience]])

predicted_salary = round(prediction[0], 2)

st.divider()

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "💰 Salary",
        f"₹ {predicted_salary} LPA"
    )

with m2:
    st.metric(
        "📈 Experience",
        f"{experience} Years"
    )

with m3:
    st.metric(
        "🛠 Skills",
        len(skills)
    )

# Salary Level
if predicted_salary >= 15:
    st.success("🟢 High Income Potential")

elif predicted_salary >= 8:
    st.warning("🟡 Strong Growth Potential")

else:
    st.error("🔴 Upskilling Recommended")

# ==========================================================
# GAUGE CHART
# ==========================================================
fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=predicted_salary,

    title={"text": "AI Salary Score"},

    gauge={
        "axis": {"range": [0,25]},
        "bar": {"color": "#7C3AED"},
        "steps": [
            {"range": [0,8], "color": "#1F2937"},
            {"range": [8,15], "color": "#312E81"},
            {"range": [15,25], "color": "#4C1D95"}
        ]
    }
))

st.plotly_chart(
    fig,
    use_container_width=True
)

