import streamlit as st


def show_ai_panel(summary):

    st.success("AI Report Generated")

    st.markdown(summary)