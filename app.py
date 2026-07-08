import streamlit as st

from services.data_service import DataService

st.set_page_config(
    page_title="InsightAI",
    layout="wide"
)


st.title("📊 InsightAI")
st.subheader("AI-Powered Business Intelligence & Data Analysis Assistant")


uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)


if uploaded_file:

    # Load dataset using DataService
    df = DataService.load_dataset(uploaded_file)


    st.success("Dataset loaded successfully!")


    # Dataset Preview
    st.subheader("👀 Dataset Preview")

    st.dataframe(
        df.head()
    )


    # Dataset Profile
    profile = DataService.profile_dataset(df)


    st.subheader("📋 Dataset Profile")


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Rows",
            profile["rows"]
        )


    with col2:
        st.metric(
            "Columns",
            profile["columns"]
        )


    with col3:
        st.metric(
            "Missing Values",
            profile["missing_values"]
        )


    with col4:
        st.metric(
            "Duplicate Rows",
            profile["duplicate_rows"]
        )


    st.subheader("🔍 Column Analysis")


    st.write(
        "Numeric Columns"
    )

    st.write(
        profile["numeric_columns"]
    )


    st.write(
        "Categorical Columns"
    )

    st.write(
        profile["categorical_columns"]
    )


    st.write(
        "Date Columns"
    )

    st.write(
        profile["date_columns"]
    )


    st.subheader("💾 Dataset Information")


    st.write(
        f"Memory Usage: {profile['memory_usage_mb']} MB"
    )