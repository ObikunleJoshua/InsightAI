import streamlit as st

from services.filter_service import FilterService


def show_filter_sidebar(df):
    """
    Display dynamic dataset filters in the sidebar.
    """

    st.sidebar.divider()

    st.sidebar.subheader("🔍 Dataset Filters")

    filter_columns = FilterService.get_filter_columns(df)

    filters = {}

    for column in filter_columns:

        options = ["All"] + sorted(
            df[column].dropna().unique().tolist()
        )

        filters[column] = st.sidebar.selectbox(
            column,
            options,
        )

    return filters