import streamlit as st
from Assets import Display
from Assets import Weight
from Assets import Speed
from Assets import Temp
from Assets import Time
from Assets import Currency
from Assets import Volume
from Assets import Number

def home_page():
    st.markdown("""
        <style>
        .centered-image {
            display: block;
            width: 100px;
            border-radius: 12px;
            display: flex;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 1);
            margin-bottom: 10px;
        }
        .weight-image {
            display: block;
            width: 100px;
            height: 100px;
            border-radius: 12px;
            display: flex;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 1);
            margin-bottom: 10px;
        }
        .stButton > button {
            appearance: button;
            background-color: #1652F0;
            border: 1px solid #1652F0;
            border-radius: 4px;
            color: #FFFFFF;
            cursor: pointer;
            width: 100px;
            line-height: 1.15;
            margin-top: 10px;
            text-align: center;
            transition: all 80ms ease-in-out;
        }
        .stButton > button:disabled {
            opacity: .5;
        }
        .stButton > button:focus {
            outline: 0;
        }
        .stButton > button:hover {
            background-color: #0A46E4;
            border-color: #0A46E4;
        }
        .stButton > button:active {
            background-color: #0039D7;
            border-color: #0039D7;
        }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    col5, col6, col7, col8 = st.columns([1, 1, 1, 1])
    
    with col1:
        st.markdown("""
            <img src="https://i.postimg.cc/VNqT2m9m/ruler.png" class="centered-image">
        """, unsafe_allow_html=True)
        if st.button("LENGTH", key="len"):
            st.session_state["page"] = "Display"
            st.rerun()

    with col2:
        st.markdown("""
            <img src="https://i.postimg.cc/XYfV1Ttv/Pngtree-pink-electronic-scale-4490130.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("WEIGHT", key="len1"):
            st.session_state["page"] = "Display_weight"
            st.rerun()

    with col3:
        st.markdown("""
            <img src="https://i.postimg.cc/2jTrPskc/vecteezy-speedometer-or-tachometer-with-arrow-infographic-gauge-9389587.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("SPEED", key="len2"):
            st.session_state["page"] = "Display_speed"
            st.rerun()

    with col4:
        st.markdown("""
            <img src="https://i.postimg.cc/Bng4TR8f/Pngtree-thermometer-icon-vector-icon-5249326.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("TEMP", key="len3"):
            st.session_state["page"] = "Display_temp"
            st.rerun()

    with col5:
        st.text("")
        st.text("")
        st.markdown("""
            <img src="https://i.postimg.cc/RVvhy37J/clock.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("TIME", key="len4"):
            st.session_state["page"] = "Display_time"
            st.rerun()

    with col6:
        st.text("")
        st.text("")
        st.markdown("""
            <img src="https://i.postimg.cc/26WCJY95/currency-conversion.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("CURRENCY", key="len5"):
            st.session_state["page"] = "Display_currency"
            st.rerun()

    with col7:
        st.text("")
        st.text("")
        st.markdown("""
            <img src="https://i.postimg.cc/7Znv5Vbm/volume.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("VOLUME", key="len6"):
            st.session_state["page"] = "Display_volume"
            st.rerun()

    with col8:
        st.text("")
        st.text("")
        st.markdown("""
            <img src="https://i.postimg.cc/SKVJfC1G/file.png" class="weight-image">
        """, unsafe_allow_html=True)
        if st.button("NUMBER", key="len7"):
            st.session_state["page"] = "Display_number"
            st.rerun()

        
    
def display_page():
    """Logic for the Display page."""
    
    st.subheader("LENGTH CONVERSION")
    
    try:
        obj = Display.Display  
        obj.display()  
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()
        
def display_weight():
   
    
    st.subheader("WEIGHT CONVERSION")
    try:
        obj = Weight.Weight  
        obj.display_weight()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()      

def display_speed():
   
    
    st.subheader("SPEED CONVERSION")
    try:
        obj = Speed.Speed
        obj.dSpeed()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()     
        

def display_temp():
   
    
    st.subheader("TEMP CONVERSION")
    try:
        obj = Temp.Temp
        obj.dTemp()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()   

def display_time():
    
    st.subheader("TIME CONVERSION")
    try:
        obj = Time.Time
        obj.d_time()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()   


def display_currency():
    
    st.subheader("CURRENCY CONVERSION")
    try:
        obj = Currency.Currency
        obj.dCurrency()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()

def display_volume():
    
    st.subheader("VOLUME CONVERSION")
    try:
        obj = Volume.Display
        obj.d_volume()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun()   

def display_number():
    
    st.subheader("CURRENCY CONVERSION")
    try:
        obj = Number.Number
        obj.d_number()
        print("hii")
    except Exception as e:
        st.error(f"Error in Display function: {e}")
    if st.button("Back"):
        st.session_state["page"] = "App"
        st.rerun() 

def main():
    
    if "page" not in st.session_state:
        st.session_state["page"] = "App"

   
    page = st.session_state["page"]
    if page == "App":
        home_page()
    elif page == "Display":
        display_page()
    elif page=="Display_weight":
        display_weight()
    elif page=="Display_speed":
        display_speed()
    elif page=="Display_temp":
        display_temp()
    elif page=="Display_time":
        display_time()
    elif page=="Display_currency":
        display_currency()
    elif page=="Display_volume":
        display_volume()
    elif page=="Display_number":
        display_number()


if __name__ == "__main__":
    main()


