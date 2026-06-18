
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📚",
    layout="wide"
)

# ---------------- HOME BUTTON ----------------
top1, top2 = st.columns([8,1])

with top2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# ---------------- HEADER ----------------
st.title("📚 AI Learning Roadmap")
st.caption("Visual roadmap for your career")

career = st.selectbox(
    "Choose Career Path",
    [
        "Data Analyst",
        "Data Engineer",
        "Data Scientist"
    ]
)

# ---------------- ROADMAPS ----------------
if career == "Data Analyst":

    roadmap = [
        ("Month 1", "Excel"),
        ("Month 2", "SQL"),
        ("Month 3", "Power BI"),
        ("Month 4", "Python"),
        ("Month 5", "Projects"),
        ("Month 6", "Interview Preparation")
    ]

elif career == "Data Engineer":

    roadmap = [
        ("Month 1", "Python"),
        ("Month 2", "SQL"),
        ("Month 3", "Pandas"),
        ("Month 4", "AWS"),
        ("Month 5", "ETL Concepts"),
        ("Month 6", "Spark")
    ]

else:

    roadmap = [
        ("Month 1", "Python"),
        ("Month 2", "Pandas + NumPy"),
        ("Month 3", "Statistics"),
        ("Month 4", "Machine Learning"),
        ("Month 5", "Deep Learning"),
        ("Month 6", "Projects")
    ]

st.divider()

# ---------------- VISUAL TIMELINE ----------------
cols = st.columns(len(roadmap))

for i, (month, topic) in enumerate(roadmap):

    with cols[i]:

        st.success("✅")

        st.markdown(
            f"""
            ### {month}

            **{topic}**
            """
        )

        if i < len(roadmap)-1:
            st.markdown("⬇️")

st.divider()

# Progress
st.subheader("Career Progress")

for month, topic in roadmap:

    st.progress(
        (roadmap.index((month, topic)) + 1) / len(roadmap),
        text=f"{month} → {topic}"
    )

st.success("Roadmap Generated Successfully 🚀")

