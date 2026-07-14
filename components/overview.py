import streamlit as st

from components.classification import show_dataset_classification
from components.health import show_health
from components.kpis import (
    show_business_kpis,
    show_review_kpis,
)


def show_overview(
    df,
    dataset_type,
    quality,
    kpis,
):
    """
    Display the Overview workspace.
    """

    show_dataset_classification(dataset_type)

    st.subheader("👀 Dataset Preview")

    st.dataframe(df.head())

    show_health(quality)

    if dataset_type["type"] == "business":
        show_business_kpis(kpis)

    elif dataset_type["type"] == "reviews":
        show_review_kpis(kpis)