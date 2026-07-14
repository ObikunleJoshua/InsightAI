import streamlit as st

# ==========================
# Services
# ==========================
from services.data_service import DataService
from services.dataset_classifier import DatasetClassifier
from services.bi_service import BusinessIntelligenceService
from services.review_service import ReviewService
from services.ai.ai_manager import AIManager
from services.export.export_manager import ExportManager

# ==========================
# Components
# ==========================
from components.classification import show_dataset_classification
from components.health import show_health
from components.header import show_header
from components.sidebar import show_sidebar
from components.overview import show_overview
from components.ai_workspace import show_ai_workspace
from components.charts_workspace import show_charts_workspace
from components.profile_workspace import show_profile_workspace
from components.analytics_workspace import show_analytics_workspace
from components.filter_sidebar import show_filter_sidebar
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

show_header()
show_sidebar()

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

filters = show_filter_sidebar(df)

from services.filter_service import FilterService

df = FilterService.apply_filters(
    df,
    filters,
)

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

if "ai_summary" not in st.session_state:
    st.session_state.ai_summary = None

if "last_dataset" not in st.session_state:
    st.session_state.last_dataset = ""

current_dataset = uploaded_file.name

# New dataset uploaded?
if current_dataset != st.session_state.last_dataset:

    st.session_state.ai_summary = None
    st.session_state.last_dataset = current_dataset

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "**Overview**",
        "**AI Report**",
        "**Charts**",
        "**Analytics**",
        "**Dataset Profile**",
    ]
)

# ==========================
# Overview
# ==========================

with tab1:

    show_overview(
        df,
        dataset_type,
        quality,
        kpis,
    )

# ==========================
# AI Report
# ==========================

with tab2:

    show_ai_workspace(
        dataset_type,
        profile,
        quality,
        kpis,
    )

# ==========================
# Charts
# ==========================

with tab3:

    show_charts_workspace(
        df,
        dataset_type,
    )


# ==========================
# Analytics
# ==========================

with tab4:

    show_analytics_workspace(
    df,
    quality,
    )


# ==========================
# Dataset Profile
# ==========================

with tab5:

    show_profile_workspace(profile)