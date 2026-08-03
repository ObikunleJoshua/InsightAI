import streamlit as st

# ==========================
# Services
# ==========================
from services.metadata_service import MetadataService
from services.filter_service import FilterService
from services.data_service import DataService
from services.dataset_classifier import DatasetClassifier
from services.bi_service import BusinessIntelligenceService
from services.review_service import ReviewService
from services.ai.ai_manager import AIManager
from services.export.export_manager import ExportManager
from services.decision.context_engine import DecisionContextEngine
from services.analyst.analyst_engine import AnalystEngine
from services.intelligence.intelligence_engine import IntelligenceEngine


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
from components.ai_settings import show_ai_settings
from components.ai_business_analyst import show_ai_business_analyst
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

metadata = MetadataService.build(df)

filters = show_filter_sidebar(df)

df = FilterService.apply_filters(
    df,
    filters,
)

dataset_type = DatasetClassifier.classify(metadata)

dataset_intelligence = metadata
quality = dataset_intelligence["quality"]

# ==========================
# Decision Context
# ==========================

decision_context = DecisionContextEngine.analyze(
    columns=df.columns.tolist()
)

st.session_state["decision_context"] = decision_context

# ==========================
# Intelligence Layer
# ==========================

intelligence = IntelligenceEngine.analyze(df)

st.session_state["intelligence"] = intelligence

# st.write(intelligence)

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

if "ai_persona" not in st.session_state:
    st.session_state.ai_persona = "Executive Advisor"

if "analysis_objective" not in st.session_state:
    st.session_state.analysis_objective = "Executive Summary"

current_dataset = uploaded_file.name

# New dataset uploaded?
if current_dataset != st.session_state.last_dataset:

    st.session_state.ai_summary = None
    st.session_state.last_dataset = current_dataset

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "**Overview**",
        "**AI Report**",
        "**Charts**",
        "**Analytics**",
        "**Dataset Profile**",
        "**AI Business Analyst**",
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
        dataset_intelligence,
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
    metadata,
    quality,
    )


# ==========================
# Dataset Profile
# ==========================

with tab5:

    show_profile_workspace(dataset_intelligence)

# ==========================
# AI Business Analyst
# ==========================

with tab6:

    decision_context = st.session_state["decision_context"]

    analyze, question = show_ai_business_analyst(
        decision_context.context
    )

    if analyze:

        with st.spinner("Analyzing your business question..."):

            try:

                response = AnalystEngine.analyze(
                    df=df,
                    dataset_type=dataset_type,
                    metadata=dataset_intelligence,
                    quality=quality,
                    kpis=kpis,
                    intelligence=st.session_state["intelligence"],
                    decision_context=decision_context,
                    persona=st.session_state.ai_persona,
                    analysis_objective=st.session_state.analysis_objective,
                    business_question=question,
                )

                st.success("Analysis Complete")

                st.markdown(response)

            except Exception as e:

                st.error(str(e))