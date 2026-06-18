```python
import streamlit as st
import sqlite3
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Search Jobs",
    page_icon="🔍",
    layout="wide"
)

# Styling
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

# Home Button
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# Header
st.title("🔍 Search Jobs")
st.caption("Find opportunities based on company and experience")

# Load Database
conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

conn.close()

# Search Box
search = st.text_input(
    "Search Job Role",
    placeholder="Data Analyst, Data Engineer..."
)

# Filters
col1, col2 = st.columns(2)

with col1:
    company_filter = st.multiselect(
        "🏢 Company",
        df["company"].unique()
    )

with col2:
    experience_filter = st.multiselect(
        "📈 Experience",
        df["experience"].unique()
    )

# Apply Filters
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if company_filter:
    filtered_df = filtered_df[
        filtered_df["company"].isin(company_filter)
    ]

if experience_filter:
    filtered_df = filtered_df[
        filtered_df["experience"].isin(experience_filter)
    ]

# Metrics
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Jobs Found", len(filtered_df))

with m2:
    st.metric("Companies", filtered_df["company"].nunique())

with m3:
    st.metric("Roles", filtered_df["title"].nunique())

st.divider()

# Results
st.subheader("Available Jobs")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download
csv = filtered_df.to_csv(index=False)

st.download_button(
    "📥 Download Results",
    csv,
    "filtered_jobs.csv",
    "text/csv"
)
```
