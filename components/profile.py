import streamlit as st


def show_profile(dataset_intelligence):

    info = dataset_intelligence["dataset_info"]
    capabilities = dataset_intelligence["capabilities"]

    st.subheader("📋 Dataset Profile")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", info["rows"])

    with col2:
        st.metric("Columns", info["columns"])

    with col3:
        st.metric(
            "Missing Values",
            sum(
                column["missing"]
                for column in dataset_intelligence["columns_profiles"]
            ),
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            info["duplicate_rows"],
        )

    st.subheader("🔍 Column Analysis")

    st.write("### Numeric Columns")
    st.write(capabilities["numeric_columns"])

    st.write("### Categorical Columns")
    st.write(capabilities["categorical_columns"])

    st.write("### Datetime Columns")
    st.write(capabilities["datetime_columns"])

    st.write("### Text Columns")
    st.write(capabilities["text_columns"])

    st.subheader("💾 Dataset Information")

    st.metric(
        "Memory Usage (MB)",
        info["memory_usage_mb"],
    )