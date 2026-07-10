import streamlit as st

# ==========================
# Services
# ==========================
from services.data_service import DataService
from services.dataset_classifier import DatasetClassifier
from services.bi_service import BusinessIntelligenceService
from services.review_service import ReviewService
from services.ai.ai_manager import AIManager

# ==========================
# Components
# ==========================
from components.classification import show_dataset_classification
from components.health import show_health
from components.kpis import (
    show_business_kpis,
    show_review_kpis,
)
from components.charts import show_charts
from components.profile import show_profile
from components.ai_panel import show_ai_panel


# ==========================
# Streamlit Configuration
# ==========================

st.set_page_config(
    page_title="InsightAI",
    page_icon="assets/icon.png",
    layout="wide"
)

col1, col2 = st.columns([1, 6])

with col1:
    st.image("assets/logo.png", width=90)

with col2:
    st.title("InsightAI")
    st.caption(
        "AI-Powered Business Intelligence & Data Analysis Platform"
    )

# ==========================
# Upload
# ==========================

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel Dataset",
    type=["csv", "xlsx"]
)

# Nothing uploaded yet
if uploaded_file is None:

    st.info(
        "👆 Upload a CSV or Excel file to begin analysis."
    )

    st.stop()

# ==========================
# Load Dataset
# ==========================

df = DataService.load_dataset(uploaded_file)

dataset_type = DatasetClassifier.classify(df)

profile = DataService.profile_dataset(df)

quality = DataService.calculate_quality_score(df)

# ==========================
# Generate KPIs
# ==========================

if dataset_type["type"] == "business":

    kpis = BusinessIntelligenceService.generate_kpis(df)

elif dataset_type["type"] == "reviews":

    kpis = ReviewService.generate_review_kpis(df)

else:

    kpis = {}


# ==========================
# Dashboard
# ==========================

show_dataset_classification(dataset_type)

st.subheader("👀 Dataset Preview")

st.dataframe(df.head())

show_health(quality)

# ==========================
# AI Session State
# ==========================

if "ai_summary" not in st.session_state:
    st.session_state.ai_summary = None

if "last_dataset" not in st.session_state:
    st.session_state.last_dataset = ""

current_dataset = uploaded_file.name

# New dataset uploaded?
if current_dataset != st.session_state.last_dataset:

    st.session_state.ai_summary = None
    st.session_state.last_dataset = current_dataset

if dataset_type["type"] == "business":

    show_business_kpis(kpis)

elif dataset_type["type"] == "reviews":

    show_review_kpis(kpis)

st.subheader("🤖 AI Analyst")

st.info(
    """
The AI Analyst runs locally using Ollama.

Generating insights may take 20–60 seconds depending on
your computer.

The report is generated only when requested.
"""
)

if st.button("🚀 Generate AI Report"):

    with st.spinner("Analyzing dataset..."):

        st.session_state.ai_summary = AIManager.generate_insights(
            dataset_type,
            profile,
            quality,
            kpis
        )

if st.session_state.ai_summary:

    show_ai_panel(
        st.session_state.ai_summary
    )
show_charts(
    df,
    dataset_type
)

show_profile(profile)