import streamlit as st

class Time:
    
  def d_time():
        
    conversion_factors = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2628000, 
        "Year": 31536000, 
        "Decade": 315360000,  
        "Century": 3153600000, 
        "Millennium": 31536000000,  
        "Microsecond": 1e-6,
        "Millisecond": 1e-3,
        "Nanosecond": 1e-9,
    }

 
    
    
    col1,col2= st.columns([2,2])
    unit= st.text_input("LENGTH", value="0") 
   
    with col1:
     option1 = st.selectbox(
     "FROM",
     [
    "Second",
    "Minute",
    "Hour",
    "Day",
    "Week",
    "Month",
    "Year",
    "Decade",
    "Century",
    "Millennium",
    "Microsecond",
    "Millisecond",
    "Nanosecond"
]
    )
    with col2:
    
     option2 = st.selectbox(
    "TO",
    [
    "Minute",
    "Second",
    "Hour",
    "Day",
    "Week",
    "Month",
    "Year",
    "Decade",
    "Century",
    "Millennium",
    "Microsecond",
    "Millisecond",
    "Nanosecond"
]
    )
    print('hello')
    
    value_in_meters = float(unit) * conversion_factors[option1]
    result = value_in_meters / conversion_factors[option2]
    print(result)
    if unit and unit != '0' and option1 != option2:
          st.write(f'''
            <p style="
                color: green;
                text-align: center;
                font-family: JetBrains Mono;
                font-size: 18px;
                font-weight: bold;
            ">
            RESULT : {unit} {option1} = {result} {option2}
            </p>
        ''', unsafe_allow_html=True)
         
