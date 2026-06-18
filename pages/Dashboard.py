import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

# Load data
df = pd.read_csv("jobs.csv")

# -----------------------------
# Filters
# -----------------------------
st.sidebar.header("Filters")

selected_company = st.sidebar.multiselect(
    "Select Company",
    options=df["company"].unique(),
    default=df["company"].unique()
)

selected_experience = st.sidebar.multiselect(
    "Select Experience",
    options=df["experience"].unique(),
    default=df["experience"].unique()
)

search_role = st.sidebar.text_input(
    "Search Job Role"
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["company"].isin(selected_company)) &
    (df["experience"].isin(selected_experience))
]

if search_role:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search_role,
            case=False
        )
    ]

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(filtered_df))

with col2:
    st.metric("Companies", filtered_df["company"].nunique())

with col3:
    st.metric("Job Roles", filtered_df["title"].nunique())

# -----------------------------
# Display Data
# -----------------------------
st.write("## Filtered Jobs")

st.dataframe(filtered_df)

# -----------------------------
# Download CSV
# -----------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="filtered_jobs.csv",
    mime="text/csv"
)