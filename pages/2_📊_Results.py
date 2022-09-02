import streamlit as st

st.set_page_config(
    page_title="Unicorn's \u2022 Results",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
# Form Results
***
Sadly I am yet to have any results to share with y'all 😥
""")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
