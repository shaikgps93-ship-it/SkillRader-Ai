import streamlit as st
from utils.db_connection import get_jobs_data

st.title("🔍 Search Jobs")

df = get_jobs_data()

search = st.text_input("Search Role")

if search:
    results = df[
        df["title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]
else:
    results = df

st.dataframe(results)