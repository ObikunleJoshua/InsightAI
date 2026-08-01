import streamlit as st


SUGGESTED_QUESTIONS = {
    "Commercial Performance": [
        "Why is profit declining?",
        "Which products should receive more investment?",
        "Which customer segment creates the most value?",
        "Which region deserves additional investment?",
    ],

    "Financial Performance": [
        "What is driving profitability?",
        "Which costs should management reduce?",
        "Where are the largest financial risks?",
        "Which business unit is underperforming?",
    ],

    "Operational Performance": [
        "Where are operational bottlenecks?",
        "Which processes require optimization?",
        "What is reducing operational efficiency?",
        "Where should automation be introduced?",
    ],

    "Workforce Performance": [
        "Which teams require attention?",
        "What workforce trends need action?",
        "How can productivity improve?",
        "What HR risks exist?",
    ],

    "Asset Performance": [
        "Which assets are underperforming?",
        "Where should maintenance be prioritized?",
        "Which assets create the highest value?",
        "What utilization improvements are possible?",
    ]
}


def show_ai_business_analyst(context):

    st.subheader("🧠 AI Business Analyst")

    st.caption(
        "Ask business questions and receive executive-level decision support."
    )

    st.info(
        f"**Decision Context:** {context}"
    )

    st.divider()

    suggestions = SUGGESTED_QUESTIONS.get(
        context,
        [
            "What are the biggest business risks?",
            "What opportunities should management explore?",
            "Which KPIs deserve immediate attention?",
            "What actions should executives prioritize?",
        ],
    )

    selected_question = st.selectbox(
        "Suggested Business Questions",
        suggestions,
    )

    question = st.text_area(
        "Or ask your own question",
        value=selected_question,
        height=120,
        placeholder="Example: Why has profitability declined over the last quarter?",
    )

    st.divider()

    analyze = st.button(
        "🔍 Analyze Question",
        use_container_width=True,
    )

    return analyze, question