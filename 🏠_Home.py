import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Unicorn's Site \u2022 Home", page_icon="🏠")
st.sidebar.success("Navigate to other pages here")
md = open("markdowns/home.md", 'r', encoding='utf-8')
st.markdown(md.read())

