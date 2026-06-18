
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

```python id="d8jy7d"
# ---------------- AI PREDICTION ----------------
prediction = model.predict([[experience]])

predicted_salary = round(prediction[0], 2)

st.divider()

# Premium Metrics
m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "💰 Predicted Salary",
        f"₹ {predicted_salary} LPA"
    )

with m2:
    st.metric(
        "📈 Experience",
        f"{experience} Years"
    )

with m3:
    st.metric(
        "🛠 Skills Selected",
        len(skills)
    )

# Salary Category
if predicted_salary >= 15:

    level = "🟢 High Income Potential"

elif predicted_salary >= 8:

    level = "🟡 Strong Growth Potential"

else:

    level = "🔴 Upskilling Recommended"

st.success(level)

# ---------------- GAUGE ----------------
fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=predicted_salary,

    title={
        "text": "AI Salary Score"
    },

    gauge={
        "axis": {
            "range": [0, 25]
        },

        "bar": {
            "color": "#7C3AED"
        },

        "steps": [
            {"range": [0, 8], "color": "#1F2937"},
            {"range": [8, 15], "color": "#312E81"},
            {"range": [15, 25], "color": "#4C1D95"}
        ]
    }
))

fig.update_layout(
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# AI Insight Card
# ==========================================================
# CAREER MATCHES
# ==========================================================
st.divider()

st.subheader("💼 Career Opportunities")

st.progress(0.95, text="Data Analyst")
st.progress(0.88, text="Business Analyst")
st.progress(0.82, text="BI Analyst")
st.progress(0.76, text="Data Engineer")

# ==========================================================
# TOP PAYING SKILLS
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
# TOP PAYING COMPANIES
# ==========================================================
st.divider()

st.subheader("🏢 Top Paying Companies")

company1, company2, company3 = st.columns(3)

with company1:
    st.metric(
        "Microsoft",
        "₹18 LPA"
    )

with company2:
    st.metric(
        "Amazon",
        "₹17 LPA"
    )

with company3:
    st.metric(
        "Accenture",
        "₹14 LPA"
    )


# ==========================================================
# SALARY GROWTH ROADMAP
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

    st.info(
        "Learn Python to increase salary opportunities."
    )

if "Python" in skills and "AWS" not in skills:

    st.info(
        "Adding AWS can significantly improve Data Engineering salaries."
    )

if "Excel" in skills and "Power BI" not in skills:

    st.info(
        "Power BI is highly recommended for BI Analyst roles."
    )

if len(skills) <= 2:

    st.warning(
        "Adding more technical skills can increase your market value."
    )
# ==========================================================
# FREE LEARNING RESOURCES
# ==========================================================
st.divider()

st.subheader("📚 Free Learning Resources")

resource1, resource2, resource3 = st.columns(3)

with resource1:

    st.link_button(
        "🐍 Learn Python",
        "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
    )

    st.link_button(
        "🗄 SQL Tutorial",
        "https://www.w3schools.com/sql/"
    )

with resource2:

    st.link_button(
        "📊 Power BI Learning",
        "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"
    )

    st.link_button(
        "☁ AWS Training",
        "https://aws.amazon.com/training/digital/"
    )

with resource3:

    st.link_button(
        "🏆 Kaggle Projects",
        "https://www.kaggle.com/"
    )

    st.link_button(
        "💻 HackerRank SQL",
        "https://www.hackerrank.com/domains/sql"
    )


# ==========================================================
# RECOMMENDED CERTIFICATIONS
# ==========================================================
st.divider()

st.subheader("🎓 Recommended Certifications")

st.success("Microsoft Power BI Data Analyst Associate")
st.success("Google Data Analytics Professional Certificate")
st.success("AWS Certified Cloud Practitioner")
st.success("Databricks Fundamentals")
st.success("Microsoft Azure Fundamentals")


# ==========================================================
# TRENDING SKILLS
# ==========================================================
st.divider()

st.subheader("🔥 Trending Skills in 2026")

trend1, trend2, trend3 = st.columns(3)

with trend1:

    st.metric(
        "Generative AI",
        "Very High Demand"
    )

    st.metric(
        "SQL",
        "High Demand"
    )

with trend2:

    st.metric(
        "Python",
        "Very High Demand"
    )

    st.metric(
        "Power BI",
        "High Demand"
    )

with trend3:

    st.metric(
        "AWS",
        "Very High Demand"
    )

    st.metric(
        "Spark",
        "Growing Fast"
    )


# ==========================================================
# FINAL AI SUMMARY
# ==========================================================
st.divider()

st.markdown(
    f"""
    <div class='glass-card'>

    <h2>🤖 AI Career Summary</h2>

    Based on your profile:

    ✅ Experience: <b>{experience} Years</b><br>
    ✅ Skills Selected: <b>{len(skills)}</b><br>
    ✅ Estimated Salary: <b>₹ {predicted_salary} LPA</b><br>

    Recommendation:

    Continue building advanced skills like AWS, Spark,
    Databricks and AI tools to maximize salary growth.

    </div>
    """,
    unsafe_allow_html=True
)

st.success("Salary Prediction Completed Successfully 🚀")
