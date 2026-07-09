import streamlit as st


def show_dataset_classification(dataset_type):

    st.success("Dataset loaded successfully!")

    st.info(
        f"""
📁 Dataset Classification

{dataset_type['label']}

Confidence Score:
{dataset_type['confidence']:.0%}
"""
    )