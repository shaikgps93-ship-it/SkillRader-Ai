import streamlit as st
import sqlite3
import pandas as pd

st.title("🔍 Search Jobs")

# Load database
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# ---------------- Search Bar ----------------
search = st.text_input(
    "Search Job Role",
    placeholder="Data Analyst, Data Engineer..."
)

# ---------------- Filters ----------------
col1, col2 = st.columns(2)

with col1:
    company_filter = st.multiselect(
        "Select Company",
        options=df["company"].unique()
    )

with col2:
    experience_filter = st.multiselect(
        "Select Experience",
        options=df["experience"].unique()
    )

# ---------------- Apply Filters ----------------
filtered_df = df.copy()

# Search role
if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# Company filter
if company_filter:
    filtered_df = filtered_df[
        filtered_df["company"].isin(company_filter)
    ]

# Experience filter
if experience_filter:
    filtered_df = filtered_df[
        filtered_df["experience"].isin(experience_filter)
    ]

# ---------------- Results ----------------
st.subheader("Available Jobs")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ---------------- Download CSV ----------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Results",
    data=csv,
    file_name="filtered_jobs.csv",
    mime="text/csv"
)

# ---------------- Metrics ----------------
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Jobs Found",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Companies",
        filtered_df["company"].nunique()
    )

with col3:
    st.metric(
        "Roles",
        filtered_df["title"].nunique()
    )

