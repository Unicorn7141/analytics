import streamlit as st
import webbrowser

pets_form_button = None

st.set_page_config(page_title="Unicorn's \u2022 Forms", page_icon="📜")
st.markdown(f"""
# Forms
***
## A short introduction and explanations
In this page you'll find all the currently available forms for you to answer.
All you have to do, is just choose which one you want to fill and a new tab will open.

A new form will be released every month here, and the summary of the previous one will be shared in the
[results](Results) page.
***

""")

st.title("Available Forms")
st.write("#### Pets Matching")
with st.expander("Explanation", True):
    st.markdown("""
    This form is going to be used in order for me to be able to build the most accurate profile to match between certain
    people and the pet they could fit the most (if at all) based on a simple questionnaire which they'll fill before
    adopting a friend.
    
    The main idea behind this project is to avoid useless death of older or "unwanted" animals in the shelters, and 
    to prevent as many issues as possible between the owners and the pets, or inside the family because of the pet.
    
    You will be required to login to your gmail account, but I am not able to see your email or your name, hence this 
    form is completely anonymous.
    ***
    **Notes**
    -
     
    1. Not every question is required
    2. Please be honest in your replies as it's going to be a part of my dataset
    3. Please share this form to as many people because the more replies I get the better and more accurate I can get.
    ***
    """)

    pets_form_button = st.button("Fill the form")

if pets_form_button:
    url = 'https://forms.gle/sN1eude7WrEtRjg16'
    webbrowser.open_new_tab(url)


st.title("Closed Forms")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)