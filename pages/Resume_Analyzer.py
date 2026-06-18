
score = int(
    (len(found_skills) / max(len(market_skills), 1)) * 100
)

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🎯 ATS Score", f"{score}%")

with c2:
    st.metric("✅ Skills Found", len(found_skills))

with c3:
    st.metric("❌ Missing Skills", len(missing_skills))

st.progress(score / 100)

# Resume Strength
if score >= 80:
    st.success("🟢 Strong Resume")

elif score >= 60:
    st.warning("🟡 Good Resume")

else:
    st.error("🔴 Resume Needs Improvement")

st.divider()

# ---------------- CAREER MATCH ----------------
st.subheader("💼 Career Match")

st.progress(0.92, text="Data Analyst")
st.progress(0.84, text="BI Analyst")
st.progress(0.71, text="Data Engineer")

st.divider()

# ---------------- FOUND SKILLS ----------------
st.subheader("✅ Skills Detected")

cols = st.columns(3)

for i, skill in enumerate(sorted(found_skills)):

    with cols[i % 3]:
        st.success(skill)

# ---------------- MISSING SKILLS ----------------
st.divider()

st.subheader("🚀 Skills To Learn")

cols = st.columns(3)

for i, skill in enumerate(sorted(list(missing_skills))[:15]):

    with cols[i % 3]:
        st.warning(f"Learn {skill}")

# ---------------- RESOURCES ----------------
st.divider()

st.subheader("📚 Free Resources")

st.link_button(
    "Learn Python",
    "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/"
)

st.link_button(
    "Learn SQL",
    "https://www.w3schools.com/sql/"
)

st.link_button(
    "Practice SQL",
    "https://www.hackerrank.com/domains/sql"
)

st.success("Resume Analysis Completed 🚀")

