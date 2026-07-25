import time
import streamlit as st

from services.ai.personas import AI_PERSONAS
from services.ai.ai_manager import AIManager
from services.export.export_manager import ExportManager
from services.ai.exceptions import AIServiceUnavailableError
from components.ai_panel import show_ai_panel


def show_ai_workspace(
    dataset_type,
    metadata,
    quality,
    kpis,
):
    """
    Display the AI Report workspace.
    """

    st.subheader("Executive Decision Workspace")

    st.caption(
        "Transform business data into strategic decisions using Artificial Intelligence."
    )

    provider = st.session_state.get(
        "ai_provider",
        "disabled",
    )

    messages = {
        "gemini": """
    ☁️ **Google Gemini (Cloud AI): Executive AI Analysis**

    InsightAI is using Google Gemini to generate executive-level business insights and strategic recommendations.

    Analysis is typically completed within a few seconds.
    """,

        "ollama": """
    💻 **Ollama (Local AI)**

    Analysis runs entirely on your local machine.

    Generation speed depends on your computer's hardware.
    """,

        "disabled": """
    🚫 **AI Disabled**

    Select an AI provider from the sidebar to generate business insights.
    """,
    }

    st.info(messages.get(provider, messages["disabled"]))

    persona = st.selectbox(
    "🧠 AI Persona",
    list(AI_PERSONAS.keys()),
    key="ai_persona",
    )

    st.caption(
        AI_PERSONAS[persona]["description"]
    )

    ANALYSIS_OBJECTIVES = [
        "Executive Summary",
        "Business Performance Review",
        "Risk Assessment",
        "Growth Opportunity Analysis",
        "Operational Improvement",
        "Digital Transformation Assessment",
        "Financial Performance Review",
    ]

    objective = st.selectbox(
        "🎯 Analysis Objective",
        ANALYSIS_OBJECTIVES,
        key="analysis_objective",
    )

    OBJECTIVE_DESCRIPTIONS = {
        "Executive Summary":
            "Provides a concise overview of the most important business findings.",

        "Business Performance Review":
            "Evaluates KPIs, operational performance, and overall business health.",

        "Risk Assessment":
            "Identifies potential risks, weaknesses, and areas requiring attention.",

        "Growth Opportunity Analysis":
            "Highlights opportunities for expansion, optimization, and increased value.",

        "Operational Improvement":
            "Focuses on improving efficiency, processes, and resource utilization.",

        "Digital Transformation Assessment":
            "Evaluates opportunities for automation, AI adoption, and digital maturity.",

        "Financial Performance Review":
            "Analyzes revenue, profitability, costs, and financial trends.",
    }

    st.caption(
        OBJECTIVE_DESCRIPTIONS[objective]
    )

    if st.button("🚀 Generate Executive Briefing"):

        with st.spinner("Analyzing business context and preparing executive recommendations..."):

            start_time = time.perf_counter()

            try:
                st.session_state.ai_summary = AIManager.generate_insights(
                    dataset_type=dataset_type,
                    metadata=metadata,
                    quality=quality,
                    kpis=kpis,
                    persona=st.session_state.ai_persona,
                    analysis_objective=st.session_state.analysis_objective,
                )

            except AIServiceUnavailableError:
                st.warning(
                    "⚠️ The AI service is temporarily unavailable. Please try again in a few moments."
                )

            except Exception:
                st.error(
                    "❌ An unexpected error occurred while generating the report."
                )

            end_time = time.perf_counter()

            st.session_state.ai_generation_time = (
                end_time - start_time
            )

    if st.session_state.ai_summary:

        provider = st.session_state.get(
            "ai_provider",
            "disabled",
        )

        provider_names = {
            "gemini": "Google Gemini",
            "ollama": "Ollama",
            "disabled": "Disabled",
        }

        model_names = {
            "gemini": "gemini-2.5-flash",
            "ollama": "qwen3:4b",
            "disabled": "-",
        }

        st.caption(
            f"""
        **Provider:** {provider_names.get(provider)}

        **Model:** {model_names.get(provider)}

        **Generation Time:** {st.session_state.ai_generation_time:.2f} seconds
    """
        )

        st.divider()

        show_ai_panel(
            st.session_state.ai_summary
        )

        st.divider()

        st.subheader("📤 Export Executive Briefing")

        export_type = st.selectbox(
            "Choose Export Format",
            [
                "Markdown",
                "DOCX",
                "PDF",
            ],
        )

        if st.button("⬇ Export Report", use_container_width=True):

            exported_file = ExportManager.export(
                report=st.session_state.ai_summary,
                filename="insightai_report",
                file_type=export_type.lower(),
            )

            st.success(
                f"Report exported successfully!\n\nSaved to:\n{exported_file}"
            )