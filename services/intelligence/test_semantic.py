import streamlit as st

from services.intelligence.semantic_discovery import (
    SemanticDiscovery,
)


def show_semantic_discovery(df):

    st.subheader("Business Semantic Discovery")

    semantics = SemanticDiscovery.discover(df)

    st.json(semantics)