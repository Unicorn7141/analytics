import streamlit as st

page_title = "Unicorn's \u2022 Home"
st.set_page_config(page_title=page_title, page_icon="🏠")
st.sidebar.success("Navigate to other pages here")
md = open("markdowns/home.md", 'r', encoding='utf-8')
st.markdown(md.read())

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
