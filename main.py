import streamlit as st
from machine_learning import show_machine_learning_page  

# Set page configuration
st.set_page_config(page_title="Energy Consumption Predictions", page_icon=":zap:", layout="wide")


if 'already_called' not in st.session_state:
    st.session_state['already_called'] = True
    st.session_state['current_page'] = 'Energy Project'  

def show_home_page():
    # Display the logo and introduction text
    st.image('transparent_bulb_logo.webp', width=150)  
    
    st.markdown(
        """
        # Welcome to the Energy Project
        
        The Energy Project is a data analyst initiative dedicated to the thorough exploration 
        and optimization of energy consumption. In the context of rapid technological 
        advancements and sustainable development challenges, our primary goal is to 
        intricately analyze national and departmental energy dynamics, focusing on risk 
        mitigation strategies for potential blackouts.
        
        Leveraging the comprehensive Open Data Energy Networks (ODRE) dataset since 2013, 
        we conduct in-depth departmental-level analyses, scrutinize production sectors, 
        and assess the geographical distribution of renewable energy sources.
        
        Explore our meticulous dataset overview, encompassing actual consumption, 
        production components, Energy Transfer Stations, and vital metrics such as TCO and TCH.
        
        For precise energy predictions, visit the Machine Learning page.
        
        Join us in shaping a sustainable and efficient future through data-driven insights 
        and informed decision-making.
        """
    )

def show_authors_page():
    # Display authors and LinkedIn links
    st.title('Authors')
    st.markdown("""
    **Maryam Moradi**  
    [LinkedIn](https://www.linkedin.com/in/maryam-moradi-92b89771/)

    **Sara Cerreto**  
    [LinkedIn](https://www.linkedin.com/in/sara-cerreto/)

    **Leena Warunkar**  
    [LinkedIn](https://www.linkedin.com/in/leena-warunkar/)
    """)

# Define a function to set the current page
def set_page(page_name):
    st.session_state['current_page'] = page_name

# Sidebar navigation with buttons
st.sidebar.title('Navigation')
if st.sidebar.button('Energy Project'):
    set_page('Energy Project')
if st.sidebar.button('Machine Learning'):
    set_page('Machine Learning')
if st.sidebar.button('Authors'):
    set_page('Authors')

# Display the selected page content
if st.session_state['current_page'] == 'Energy Project':
    show_home_page()
elif st.session_state['current_page'] == 'Machine Learning':
    show_machine_learning_page()  
elif st.session_state['current_page'] == 'Authors':
    show_authors_page()
