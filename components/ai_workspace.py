import time
import streamlit as st

from services.ai.ai_manager import AIManager
from services.export.export_manager import ExportManager
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

    st.subheader("🤖 AI Analyst")

    provider = st.session_state.get(
        "ai_provider",
        "disabled",
    )

    messages = {
        "gemini": """
    ☁️ **Google Gemini (Cloud AI)**

    Analysis is performed securely using Google's Gemini API.

    Reports are typically generated within a few seconds.
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

    if st.button("🚀 Generate AI Report"):

        with st.spinner("Analyzing dataset..."):

            start_time = time.perf_counter()

            st.session_state.ai_summary = AIManager.generate_insights(
                dataset_type,
                metadata,
                quality,
                kpis,
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

        st.subheader("📤 Export Report")

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