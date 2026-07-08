import streamlit as st

from services.data_service import DataService
from services.bi_service import BusinessIntelligenceService
from services.dataset_classifier import DatasetClassifier
from services.chart_service import ChartService
from services.review_service import ReviewService


st.set_page_config(
    page_title="InsightAI",
    layout="wide"
)


# ==========================
# UI Functions
# ==========================

def show_dataset_classification(dataset_type):

    st.success("Dataset loaded successfully!")

    st.info(
        f"""
📁 Dataset Classification

{dataset_type['label']}

Confidence Score:
{dataset_type['confidence']:.0%}
"""
    )


def show_health(quality):

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
            st.warning(
                f"⚠️ {issue}"
            )

    else:
        st.success(
            "✅ No data quality issues detected."
        )


def show_business_kpis(kpis):

    st.subheader("📊 Business KPIs")

    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Total Sales",
            f"${kpis.get('total_sales',0):,.2f}"
        )

    with col2:
        st.metric(
            "Total Profit",
            f"${kpis.get('total_profit',0):,.2f}"
        )

    with col3:
        st.metric(
            "Total Orders",
            kpis.get("total_orders",0)
        )

    with col4:
        st.metric(
            "Average Order Value",
            f"${kpis.get('average_order_value',0):,.2f}"
        )


def show_review_kpis(kpis):

    st.subheader("⭐ Review KPIs")

    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Total Reviews",
            kpis.get("total_reviews",0)
        )

    with col2:
        st.metric(
            "Average Rating",
            kpis.get("average_rating","N/A")
        )

    with col3:
        st.metric(
            "Recommendation Rate",
            f"{kpis.get('recommendation_rate',0)}%"
        )

    with col4:
        st.metric(
            "Top Department",
            kpis.get("top_department","N/A")
        )


def show_charts(df, dataset_type):

    st.subheader("📈 Visual Analytics")


    if dataset_type["type"] == "business":

        chart = ChartService.sales_by_region(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )


        chart = ChartService.sales_by_category(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )


    elif dataset_type["type"] == "reviews":

        chart = ChartService.ratings_distribution(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )


def show_profile(profile):

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
        "### Numeric Columns"
    )

    st.write(
        profile["numeric_columns"]
    )


    st.write(
        "### Categorical Columns"
    )

    st.write(
        profile["categorical_columns"]
    )


    st.subheader("💾 Dataset Information")


    st.metric(
        "Memory Usage (MB)",
        profile["memory_usage_mb"]
    )


# ==========================
# Main Application
# ==========================

st.title("📊 InsightAI")

st.subheader(
    "AI-Powered Business Intelligence & Data Analysis Assistant"
)


uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)


if uploaded_file:

    df = DataService.load_dataset(
        uploaded_file
    )


    dataset_type = DatasetClassifier.classify(
        df
    )


    profile = DataService.profile_dataset(
        df
    )


    quality = DataService.calculate_quality_score(
        df
    )


    st.subheader("👀 Dataset Preview")

    st.dataframe(
        df.head()
    )


    show_dataset_classification(
        dataset_type
    )


    show_health(
        quality
    )


    if dataset_type["type"] == "business":

        kpis = BusinessIntelligenceService.generate_kpis(df)

        show_business_kpis(
            kpis
        )


    elif dataset_type["type"] == "reviews":

        kpis = ReviewService.generate_review_kpis(df)

        show_review_kpis(
            kpis
        )


    show_charts(
        df,
        dataset_type
    )


    show_profile(
        profile
    )