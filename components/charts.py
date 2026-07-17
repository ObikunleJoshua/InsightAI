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
        else:
            st.info(
                "Sales by Region chart is unavailable because the required columns could not be identified."
            )

        chart = ChartService.sales_by_category(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )
        else:
            st.info(
                "Sales by Category chart is unavailable because the required columns could not be identified."
            )

    elif dataset_type["type"] == "reviews":

        chart = ChartService.ratings_distribution(df)

        if chart:
            st.plotly_chart(
                chart,
                use_container_width=True
            )
        else:
            st.info(
                "No rating column was found for this dataset."
            )

    else:
        st.info(
            "No predefined charts are available for this dataset type."
        )