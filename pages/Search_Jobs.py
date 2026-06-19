from serpapi import GoogleSearch
import pandas as pd

API_KEY = "7d2c5abba845c2d99003ac20a0110e9e075b067c1d20e374629b1ef7375c1978"

params = {
    "engine": "google_jobs",
    "q": "Data Analyst",
    "location": "India",
    "hl": "en",
    "api_key": API_KEY
}

search = GoogleSearch(params)
results = search.get_dict()

job_list = []

for job in results.get("jobs_results", []):

    job_list.append({
        "Title": job.get("title"),
        "Company": job.get("company_name"),
        "Location": job.get("location"),
        "Apply Link": job.get("related_links", [{}])[0].get("link", "")
    })

df = pd.DataFrame(job_list)

st.data_editor(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Apply Link": st.column_config.LinkColumn(
            "Apply 🚀",
            display_text="Open"
        )
    }
)
