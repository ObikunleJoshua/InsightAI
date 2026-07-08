import streamlit as st
import pandas as pd

from agent import ask_agent
from data_tools import generate_dataset_summary

st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

st.title("📊 AI Data Analyst Agent")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # Preview
    st.subheader("Preview")
    st.dataframe(df.head())

    # Dataset Info
    st.subheader("Dataset Information")

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.write("Column Names:")
    st.write(df.columns.tolist())

    # Generate Summary
    summary = generate_dataset_summary(df)

    # Quick Insights
    st.subheader("Quick Insights")
    st.json(summary)

    # AI Section
    st.subheader("Ask the AI")

    question = st.text_input(
        "Ask a question about this dataset"
    )

    if st.button("Analyze"):

        with st.spinner("Analyzing..."):

            answer = ask_agent(
                question,
                summary
            )

        st.subheader("AI Analysis")
        st.write(answer)