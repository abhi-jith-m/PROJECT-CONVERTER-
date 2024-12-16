import streamlit as st
from App import *


st.set_page_config(page_title="CONVERTER", page_icon="https://i.postimg.cc/t4KLvMwq/loop-arrow.png")
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name

# Initialize session state

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Unit Conversion"


# Display the current page
if st.session_state["current_page"] == "Unit Conversion":
    
    st.markdown("""
     
     <div style="display: flex; align-items: center; justify-content: center; margin-top:-30px">
        <img src="https://i.postimg.cc/43CpK672/repost.png" style="width: 50px; height: 50px; margin-right: 10px;" />
        <h1 style="color: white; font-family: 'Moonrising'; font-size: 48px;">UNIT CONVERTER</h1>
    </div>
        """, unsafe_allow_html=True)
    
    
    st.text("")
    st.text("")
    
    main()
