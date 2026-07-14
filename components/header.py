import streamlit as st


def show_header():
    """
    Display the application header.
    """

    col1, col2 = st.columns([1, 7])

    with col1:
        st.image("assets/logo.png", width=90)

    with col2:
        st.title("InsightAI")
        st.markdown("**Data Intelligence Platform**")
        st.caption("Version 0.1.0")

    st.divider()