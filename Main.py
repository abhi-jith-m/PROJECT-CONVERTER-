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
    st.title("UNIT CONVERSION")
    st.text("")
    st.text("")
    
    main()
