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
                metadata,
                quality,
                kpis,
            )

    if st.session_state.ai_summary:

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