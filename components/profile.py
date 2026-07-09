import streamlit as st

def show_profile(profile):

    st.subheader("📋 Dataset Profile")


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Rows",
            profile["rows"]
        )

    with col2:
        st.metric(
            "Columns",
            profile["columns"]
        )

    with col3:
        st.metric(
            "Missing Values",
            profile["missing_values"]
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            profile["duplicate_rows"]
        )


    st.subheader("🔍 Column Analysis")


    st.write(
        "### Numeric Columns"
    )

    st.write(
        profile["numeric_columns"]
    )


    st.write(
        "### Categorical Columns"
    )

    st.write(
        profile["categorical_columns"]
    )


    st.subheader("💾 Dataset Information")


    st.metric(
        "Memory Usage (MB)",
        profile["memory_usage_mb"]
    )
