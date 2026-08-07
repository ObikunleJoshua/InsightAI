import streamlit as st

from .ui import ExecutiveUI


class ExecutiveSnapshot:

    @staticmethod
    def render(
        decision_context: str,
        persona: str,
        quality: str,
        confidence: str,
    ):

        ExecutiveUI.section(
            "Executive Snapshot",
            "📌",
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            ExecutiveUI.metric(
                "🎯 Decision Context",
                decision_context,
            )

        with col2:
            ExecutiveUI.metric(
                "🧠 AI Persona",
                persona,
            )

        with col3:
            ExecutiveUI.metric(
                "📈 Dataset Quality",
                quality,
            )

        with col4:
            ExecutiveUI.metric(
                "📊 Confidence",
                confidence,
            )

        ExecutiveUI.spacer(10)

        st.markdown("---")