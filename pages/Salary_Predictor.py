
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


# ==========================================================
# AI INSIGHT CARD
# ==========================================================
st.markdown(
    f"""
    <div class='glass-card'>

    <h2>🧠 AI Insight</h2>

    Based on your experience and skills, your estimated
    market salary is:

    <h1>₹ {predicted_salary} LPA</h1>

    Continue learning high-value skills to maximize growth.

    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# CAREER OPPORTUNITIES
# ==========================================================
st.divider()

st.subheader("💼 Career Opportunities")

st.progress(0.95, text="Data Analyst")
st.progress(0.88, text="Business Analyst")
st.progress(0.82, text="BI Analyst")
st.progress(0.76, text="Data Engineer")

# ==========================================================
# HIGH VALUE SKILLS
# ==========================================================
st.divider()

st.subheader("💎 High-Value Skills")

col1, col2 = st.columns(2)

with col1:

    st.success("AWS → +20% Salary Growth")
    st.success("Spark → +15% Salary Growth")
    st.success("Airflow → +12% Salary Growth")

with col2:

    st.success("Docker → +10% Salary Growth")
    st.success("Snowflake → +18% Salary Growth")
    st.success("Databricks → +22% Salary Growth")

# ==========================================================
# TOP COMPANIES
# ==========================================================
st.divider()

st.subheader("🏢 Top Paying Companies")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Microsoft", "₹18 LPA")

with c2:
    st.metric("Amazon", "₹17 LPA")

with c3:
    st.metric("Accenture", "₹14 LPA")

# ==========================================================
# SALARY JOURNEY
# ==========================================================
st.divider()

st.subheader("📈 Salary Growth Journey")

st.progress(0.20, text="0 Years → ₹5 LPA")
st.progress(0.40, text="2 Years → ₹8 LPA")
st.progress(0.60, text="4 Years → ₹12 LPA")
st.progress(0.80, text="6 Years → ₹16 LPA")
st.progress(1.00, text="8+ Years → ₹22 LPA")

# ==========================================================
# AI RECOMMENDATIONS
# ==========================================================
st.divider()

st.subheader("🚀 AI Recommendations")

if "SQL" in skills and "Python" not in skills:
    st.info("Learn Python to unlock more opportunities.")

if "Python" in skills and "AWS" not in skills:
    st.info("AWS can significantly boost Data Engineering salaries.")

if "Excel" in skills and "Power BI" not in skills:
    st.info("Power BI is highly recommended for BI Analyst roles.")

if len(skills) <= 2:
    st.warning("Adding more technical skills increases market value.")

# ==========================================================
# FREE RESOURCES
# ==========================================================
st.divider()

st.subheader("📚 Free Learning Resources")

st.link_button(
    "🐍 Python Course",
    "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
)

st.link_button(
    "🗄 SQL Tutorial",
    "https://www.w3schools.com/sql/"
)

st.link_button(
    "☁ AWS Training",
    "https://aws.amazon.com/training/digital/"
)

st.link_button(
    "🏆 Kaggle Projects",
    "https://www.kaggle.com/"
)

# ==========================================================
# CERTIFICATIONS
# ==========================================================
st.divider()

st.subheader("🎓 Recommended Certifications")

st.success("Google Data Analytics Professional Certificate")
st.success("Microsoft Power BI Data Analyst Associate")
st.success("AWS Cloud Practitioner")
st.success("Databricks Fundamentals")

# ==========================================================
# TRENDING SKILLS
# ==========================================================
st.divider()

st.subheader("🔥 Trending Skills")

st.metric("Generative AI", "Very High Demand")
st.metric("Python", "Very High Demand")
st.metric("AWS", "High Demand")
st.metric("Spark", "Growing Fast")

# ==========================================================
# FINAL SUMMARY
# ==========================================================
st.divider()

st.markdown(
    f"""
    <div class='glass-card'>

    <h2>🤖 AI Career Summary</h2>

    ✅ Experience: {experience} Years<br>
    ✅ Skills Selected: {len(skills)}<br>
    ✅ Estimated Salary: ₹ {predicted_salary} LPA<br>

    Recommendation:

    Continue building advanced skills like AWS,
    Spark, Databricks and AI tools.

    </div>
    """,
    unsafe_allow_html=True
)

st.success("Salary Prediction Completed Successfully 🚀")

