import streamlit as st

from services.ai.provider_registry import ProviderRegistry

def show_ai_settings():
    """Display AI provider selection."""

    providers = ProviderRegistry.get_provider_options()

    # Create session state if it doesn't exist
    if "ai_provider" not in st.session_state:
        st.session_state.ai_provider = "gemini"

    current_provider = st.session_state.ai_provider

    # Find which option should be selected
    options = list(providers.keys())
    values = list(providers.values())

    if current_provider in values:
        index = values.index(current_provider)
    else:
        index = 0

    selected = st.sidebar.selectbox(
        "AI Provider",
        options,
        index=index,
    )

    st.session_state.ai_provider = providers[selected]