# authors.py
import streamlit as st

def show_authors_page():
    st.title('Authors')

    
    st.markdown("""
    ### Maryam Moradi
    [LinkedIn](https://www.linkedin.com/in/maryam-moradi-92b89771/)

    ### Sara Cerreto
    [LinkedIn](https://www.linkedin.com/in/sara-cerreto/)

    ### Leena Warunkar
    [LinkedIn](https://www.linkedin.com/in/leena-warunkar/)
    """, unsafe_allow_html=True)