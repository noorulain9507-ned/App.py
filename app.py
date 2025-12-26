import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Workflow & Report Generator",
    layout="centered"
)   

# ---------------- TITLE ----------------
st.title("📊 AI Workflow & Report Generator")
st.caption("Upload a CSV file and generate business insights")

st.divider()

# ---------------- FILE UPLOADER ----------------
st.subheader("📁 Upload Your Data")

uploaded_file = st.file_uploader(
    "Upload a CSV file only",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

else:
    st.info("Please upload a CSV file to continue.")

st.divider()

# ---------------- BUTTONS ----------------
st.subheader("⚙️ Generate Insights")

col1, col2, col3 = st.columns(3)

with col1:
    btn_summary = st.button("📌 Summarize Trends")

with col2:
    btn_anomaly = st.button("🚨 Identify Anomalies")

with col3:
    btn_actions = st.button("💡 Suggest Actions")

st.divider()

# ---------------- OUTPUT CONTAINERS ----------------
summary_container = st.container()
anomaly_container = st.container()
action_container = st.container()

# ---------------- OUTPUT: SUMMARY ----------------
with summary_container:
    if btn_summary:
        if uploaded_file:
            st.subheader("📌 Trend Summary")
            st.info(
                "- Overall trends will appear here\n"
                "- Example: Sales increased over time\n"
                "- Example: High-performing products identified"
            )
        else:
            st.error("Please upload a CSV file first.")

# ---------------- OUTPUT: ANOMALIES ----------------
with anomaly_container:
    if btn_anomaly:
        if uploaded_file:
            st.subheader("🚨 Anomaly Report")
            st.warning(
                "- Unusual patterns detected\n"
                "- Example: Sudden drop in sales\n"
                "- Example: Unexpected spikes"
            )
        else:
            st.error("Please upload a CSV file first.")

# ---------------- OUTPUT: ACTIONS ----------------
with action_container:
    if btn_actions:
        if uploaded_file:
            st.subheader("💡 Recommended Business Actions")
            st.success(
                "1. Improve forecasting strategy\n"
                "2. Investigate abnormal values\n"
                "3. Optimize business operations"
            )
        else:
            st.error("Please upload a CSV file first.")

# ---------------- WARNINGS & LIMITATIONS ----------------
st.divider()
st.subheader("⚠️ Warnings & Limitations")

st.markdown("""
- This tool provides **AI-generated insights**, not professional advice.
- Results depend on the **quality of uploaded data**.
- Anomalies are **indicators**, not confirmed errors.
- Large datasets may increase processing time.
""")

