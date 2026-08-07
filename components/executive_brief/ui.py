import streamlit as st


class ExecutiveUI:

    SECTION_SIZE = "26px"
    TITLE_SIZE = "18px"
    BODY_SIZE = "15px"
    CAPTION_SIZE = "13px"

    @staticmethod
    def section(title: str, icon: str = ""):

        st.markdown(
            f"""
            <h2 style="
                margin:35px 0 20px 0;
                font-size:{ExecutiveUI.SECTION_SIZE};
                font-weight:700;
                color:#F3F4F6;
            ">
                {icon} {title}
            </h2>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def metric(title: str, value: str):

        with st.container(border=True):

            st.caption(title)

            st.markdown(
                f"""
                <div style="
                    font-size:22px;
                    font-weight:700;
                    line-height:1.3;
                    margin-top:8px;
                    word-break:break-word;
                ">
                    {value}
                </div>
                """,
                unsafe_allow_html=True,
            )

    @staticmethod
    def card(title: str):

        st.markdown(
            f"""
            <div style="
                font-size:{ExecutiveUI.TITLE_SIZE};
                font-weight:700;
                margin-bottom:15px;
            ">
                {title}
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def label(text: str):

        st.markdown(
            f"""
            <div style="
                font-size:14px;
                font-weight:700;
                color:#9CA3AF;
                margin-top:16px;
                margin-bottom:6px;
                text-transform:uppercase;
                letter-spacing:.5px;
            ">
                {text}
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def divider():

        st.divider()

    @staticmethod
    def bullet(text: str):

        st.markdown(
            f"""
            - {text}
            """
        )

    @staticmethod
    def question(text: str):

        st.info(text)

    @staticmethod
    def badge(text: str, color="#22C55E"):

        st.markdown(
            f"""
            <span style="
                display:inline-block;
                padding:4px 10px;
                border-radius:999px;
                background:{color}22;
                color:{color};
                font-size:11px;
                font-weight:700;
                text-transform:uppercase;
                letter-spacing:.5px;
            ">
                {text}
            </span>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def spacer(height=15):

        st.markdown(
            f"<div style='height:{height}px'></div>",
            unsafe_allow_html=True,
        )