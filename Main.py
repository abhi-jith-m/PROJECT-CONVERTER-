import streamlit as st
from App import *
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name

# Initialize session state
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Unit Conversion"

# Sidebar buttons for navigation
# with st.sidebar:
#     if st.button("Unit Conversion"):
#         navigate_to_page("Unit Conversion")
#     if st.button("About"):
#         navigate_to_page("About")
#     if st.button("Contact"):
#         navigate_to_page("Contact")

# Display the current page
if st.session_state["current_page"] == "Unit Conversion":
    st.title("UNIT CONVERSION")
    st.text("")
    st.text("")
    
    main()
# elif st.session_state["current_page"] == "About":
#     st.title("About Page")
#     st.write("This is the about page.")
# elif st.session_state["current_page"] == "Contact":
#     st.title("Contact Page")
#     st.write("Get in touch on the contact page.")
