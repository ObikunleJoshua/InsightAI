import streamlit as st


def show_business_kpis(kpis):

    st.subheader("📊 Business KPIs")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Sales",
            f"${kpis.get('total_sales',0):,.2f}"
        )

    with col2:
        st.metric(
            "Total Profit",
            f"${kpis.get('total_profit',0):,.2f}"
        )

    with col3:
        st.metric(
            "Total Orders",
            kpis.get("total_orders",0)
        )

    with col4:
        st.metric(
            "Average Order Value",
            f"${kpis.get('average_order_value',0):,.2f}"
        )


def show_review_kpis(kpis):

    st.subheader("⭐ Review KPIs")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Reviews",
            kpis.get("total_reviews",0)
        )

    with col2:
        st.metric(
            "Average Rating",
            kpis.get("average_rating","N/A")
        )

    with col3:
        st.metric(
            "Recommendation Rate",
            f"{kpis.get('recommendation_rate',0)}%"
        )

    with col4:
        st.metric(
            "Top Department",
            kpis.get("top_department","N/A")
        )