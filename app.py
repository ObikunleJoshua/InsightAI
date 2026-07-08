import streamlit as st

from services.data_service import DataService
from services.bi_service import BusinessIntelligenceService
from services.dataset_classifier import DatasetClassifier


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

    # ==========================
    # Load Dataset
    # ==========================
    df = DataService.load_dataset(uploaded_file)
    dataset_type = DatasetClassifier.classify(df)

    st.success("Dataset loaded successfully!")
    st.info(f"📁 Dataset Type: {dataset_type}")

    # ==========================
    # Generate Intelligence
    # ==========================
    profile = DataService.profile_dataset(df)
    quality = DataService.calculate_quality_score(df)
    kpis = BusinessIntelligenceService.generate_kpis(df)

    # ==========================
    # Dataset Preview
    # ==========================
    st.subheader("👀 Dataset Preview")
    st.dataframe(df.head())

    # ==========================
    # Dataset Health
    # ==========================
    st.subheader("🏥 Dataset Health")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Quality Score",
            f"{quality['score']}%"
        )

    with col2:
        st.metric(
            "Status",
            quality["quality"]
        )

    if quality["issues"]:
        for issue in quality["issues"]:
            st.warning(f"⚠️ {issue}")
    else:
        st.success("✅ No data quality issues detected.")

    # ==========================
    # Business KPIs
    # ==========================
    st.subheader("📊 Business KPIs")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Sales",
            f"${kpis.get('total_sales', 0):,.2f}"
        )

    with col2:
        st.metric(
            "Total Profit",
            f"${kpis.get('total_profit', 0):,.2f}"
        )

    with col3:
        st.metric(
            "Total Orders",
            kpis.get("total_orders", 0)
        )

    with col4:
        st.metric(
            "Average Order Value",
            f"${kpis.get('average_order_value', 0):,.2f}"
        )

    # ==========================
    # Business Leaders
    # ==========================
    st.subheader("🏆 Business Leaders")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Top Region",
            kpis.get("top_region", "N/A")
        )

    with col2:
        st.metric(
            "Top Category",
            kpis.get("top_category", "N/A")
        )

    # ==========================
    # Dataset Profile
    # ==========================
    st.subheader("📋 Dataset Profile")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", profile["rows"])

    with col2:
        st.metric("Columns", profile["columns"])

    with col3:
        st.metric("Missing Values", profile["missing_values"])

    with col4:
        st.metric("Duplicate Rows", profile["duplicate_rows"])

    # ==========================
    # Column Analysis
    # ==========================
    st.subheader("🔍 Column Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Numeric Columns")
        st.write(profile["numeric_columns"])

    with col2:
        st.write("### Categorical Columns")
        st.write(profile["categorical_columns"])

    if profile["date_columns"]:
        st.write("### Date Columns")
        st.write(profile["date_columns"])

    # ==========================
    # Dataset Information
    # ==========================
    st.subheader("💾 Dataset Information")

    st.metric(
        "Memory Usage (MB)",
        profile["memory_usage_mb"]
    )