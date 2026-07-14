import streamlit as st


def show_health(quality):

    st.subheader("🏥 Dataset Health")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Quality Score",
            f"{quality['score']}%"
        )

    with col2:
        st.metric(
            "Status",
            quality["grade"]
        )

    if quality["issues"]:

        for issue in quality["issues"]:
            st.warning(f"⚠️ {issue}")

    else:

        st.success(
            "✅ No data quality issues detected."
        )