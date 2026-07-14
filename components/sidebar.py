import streamlit as st

from services.ai.config import AI_PROVIDER


def show_sidebar():
    """
    Display the application sidebar.
    """

    with st.sidebar:

        st.image("assets/icon.png", width=80)

        st.title("InsightAI")

        st.caption("Version 0.1.0")

        st.divider()

        st.subheader("⚙️ Settings")

        st.info(
            f"""
**AI Provider**

{AI_PROVIDER.upper()}
"""
        )

        st.divider()

        st.subheader("ℹ️ About")

        st.write(
            """
InsightAI is an AI-powered Business Intelligence platform
designed to transform datasets into actionable insights.

Developed by Joshua OBIKUNLE.
"""
        )