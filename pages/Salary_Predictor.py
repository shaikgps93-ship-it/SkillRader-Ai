```python
import streamlit as st
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.title("💰 AI Salary Predictor")

# Load data
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Convert columns
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

# Train model
X = df[["experience_value"]]
y = df["salary_value"]

model = LinearRegression()
model.fit(X, y)

# User Inputs
col1, col2 = st.columns(2)

with col1:
    experience = st.slider(
        "Years of Experience",
        1,
        10,
        2
    )

with col2:
    skills = st.multiselect(
        "Skills",
        ["SQL", "Python", "Power BI", "AWS", "Excel"]
    )

# Prediction
prediction = model.predict([[experience]])

st.divider()

# Salary Card
st.metric(
    "Predicted Salary",
    f"₹ {prediction[0]:.2f} LPA"
)

# Gauge Chart
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

# Suggestions
st.subheader("🚀 Recommendations")

if "SQL" in skills and "Python" not in skills:
    st.info("Learn Python to increase salary potential.")

if "Python" in skills and "AWS" not in skills:
    st.info("Learn AWS for Data Engineering roles.")

if "Excel" in skills and "Power BI" not in skills:
    st.info("Learn Power BI for BI Analyst roles.")
```
