import streamlit as st

from services.chart_service import ChartService


def show_charts(df, dataset_type):

    st.subheader("📈 Visual Analytics")

    if dataset_type["type"] == "business":

        chart = ChartService.sales_by_region(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )

        chart = ChartService.sales_by_category(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )

    elif dataset_type["type"] == "reviews":

        chart = ChartService.ratings_distribution(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )