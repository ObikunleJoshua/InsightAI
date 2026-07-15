import streamlit as st
import plotly.express as px

from services.analytics_service import AnalyticsService


def show_analytics_workspace(
    df,
    metadata,
    quality,
):
    """
    Display advanced analytics for the dataset.
    """

    st.subheader("📉 Correlation Analysis")

    correlation = AnalyticsService.correlation_matrix(df)

    if correlation.empty:

        st.info(
            "Correlation analysis requires at least two numeric columns."
        )

        return

    insight = AnalyticsService.calculate_insight_score(
        df,
        metadata,
        quality,
    )

    st.subheader("🧠 Insight Score™")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.metric(
            "Overall Score",
            f"{insight['score']}/100",
        )

    with col2:

        st.metric(
            "Dataset Rating",
            insight["rating"],
        )

    st.progress(insight["score"] / 100)

    st.divider()

    st.write(
        """
The heatmap below shows the Pearson correlation coefficient
between all numeric columns.
"""
    )

    fig = px.imshow(
        correlation,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Correlation Heatmap",
    )

    fig.update_layout(
        height=650,
        margin=dict(l=20, r=20, t=60, b=20),
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    with st.expander("View Correlation Matrix"):

        st.dataframe(
            correlation,
            use_container_width=True,
        )

    st.divider()

    st.divider()

    st.caption("Score Breakdown")

    for item, value in insight["breakdown"].items():
        st.write(f"**{item}**: {value}")

    st.subheader("🚨 Outlier Detection")

    outliers = AnalyticsService.detect_outliers(df)

    columns = st.columns(4)

    index = 0

    for column_name, count in outliers.items():

        with columns[index % 4]:

            st.metric(
                label=column_name,
                value=count,
                help="Potential outliers detected using the IQR method.",
            )

        index += 1

    st.divider()

    st.subheader("📊 Distribution Analysis")

    numeric_columns = AnalyticsService.get_numeric_columns(metadata)

    selected_column = st.selectbox(
        "Select a numeric column",
        numeric_columns,
    )

    col1, col2 = st.columns(2)

    with col1:

        histogram = px.histogram(
            df,
            x=selected_column,
            nbins=30,
            title=f"Distribution of {selected_column}",
        )

        st.plotly_chart(
            histogram,
            use_container_width=True,
        )

    with col2:

        box_plot = px.box(
            df,
            y=selected_column,
            title=f"Box Plot of {selected_column}",
        )

        st.plotly_chart(
            box_plot,
            use_container_width=True,
        )

    