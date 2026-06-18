import streamlit as st
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression

st.title("💰 AI Salary Predictor")

# Load data
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Convert salary column
df["salary_value"] = (
    df["salary"]
    .str.replace(" LPA", "", regex=False)
    .astype(float)
)

# Convert experience
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

# User input
experience = st.slider(
    "Years of Experience",
    1,
    10,
    2
)

prediction = model.predict([[experience]])

st.metric(
    "Predicted Salary",
    f"₹ {prediction[0]:.2f} LPA"
)

# Show training data
st.subheader("Training Dataset")

st.dataframe(
    df[
        [
            "company",
            "title",
            "experience",
            "salary"
        ]
    ]
)