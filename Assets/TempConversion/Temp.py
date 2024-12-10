import streamlit as st
import streamlit as st

class Temp:
    
    def dTemp():
        
      
        conversion_factors = {
            
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Celsius", "Rankine"): lambda x: (x + 273.15) * 9/5,
        ("Celsius", "Delisle"): lambda x: (100 - x) * 3/2,
        ("Celsius", "Newton"): lambda x: x * 33/100,
        ("Celsius", "Reaumur"): lambda x: x * 4/5,
        ("Celsius", "Romer"): lambda x: (x * 21/40) + 7.5,

        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Fahrenheit", "Rankine"): lambda x: x + 459.67,
        ("Fahrenheit", "Delisle"): lambda x: (212 - x) * 5/6,
        ("Fahrenheit", "Newton"): lambda x: (x - 32) * 11/60,
        ("Fahrenheit", "Reaumur"): lambda x: (x - 32) * 4/9,
        ("Fahrenheit", "Romer"): lambda x: (x - 32) * 7/24 + 7.5,

        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        ("Kelvin", "Rankine"): lambda x: x * 9/5,
        ("Kelvin", "Delisle"): lambda x: (373.15 - x) * 3/2,
        ("Kelvin", "Newton"): lambda x: (x - 273.15) * 33/100,
        ("Kelvin", "Reaumur"): lambda x: (x - 273.15) * 4/5,
        ("Kelvin", "Romer"): lambda x: (x - 273.15) * 21/40 + 7.5,

        ("Rankine", "Celsius"): lambda x: (x - 491.67) * 5/9,
        ("Rankine", "Fahrenheit"): lambda x: x - 459.67,
        ("Rankine", "Kelvin"): lambda x: x * 5/9,
        ("Rankine", "Delisle"): lambda x: (671.67 - x) * 5/6,
        ("Rankine", "Newton"): lambda x: (x - 491.67) * 11/60,
        ("Rankine", "Reaumur"): lambda x: (x - 491.67) * 4/9,
        ("Rankine", "Romer"): lambda x: (x - 491.67) * 7/24 + 7.5,

        ("Delisle", "Celsius"): lambda x: 100 - x * 2/3,
        ("Delisle", "Fahrenheit"): lambda x: 212 - x * 5/6,
        ("Delisle", "Kelvin"): lambda x: 373.15 - x * 2/3,
        ("Delisle", "Rankine"): lambda x: 671.67 - x * 5/6,
        ("Delisle", "Newton"): lambda x: (100 - x) * 11/66,
        ("Delisle", "Reaumur"): lambda x: (100 - x) * 4/5,
        ("Delisle", "Romer"): lambda x: (100 - x) * 7/40 + 7.5,

        ("Newton", "Celsius"): lambda x: x * 100/33,
        ("Newton", "Fahrenheit"): lambda x: (x * 60/11) + 32,
        ("Newton", "Kelvin"): lambda x: (x * 100/33) + 273.15,
        ("Newton", "Rankine"): lambda x: (x * 60/11) + 491.67,
        ("Newton", "Delisle"): lambda x: (33 - x) * 2/3,
        ("Newton", "Reaumur"): lambda x: x * 4/5,
        ("Newton", "Romer"): lambda x: (x * 7/40) + 7.5,

        ("Reaumur", "Celsius"): lambda x: x * 5/4,
        ("Reaumur", "Fahrenheit"): lambda x: (x * 9/4) + 32,
        ("Reaumur", "Kelvin"): lambda x: (x * 5/4) + 273.15,
        ("Reaumur", "Rankine"): lambda x: (x * 9/4) + 491.67,
        ("Reaumur", "Delisle"): lambda x: (80 - x) * 3/2,
        ("Reaumur", "Newton"): lambda x: x * 25/16,
        ("Reaumur", "Romer"): lambda x: (x * 21/16) + 7.5,

        ("Romer", "Celsius"): lambda x: (x - 7.5) * 40/21,
        ("Romer", "Fahrenheit"): lambda x: (x - 7.5) * 24/7 + 32,
        ("Romer", "Kelvin"): lambda x: (x - 7.5) * 40/21 + 273.15,
        ("Romer", "Rankine"): lambda x: (x - 7.5) * 9/7 + 491.67,
        ("Romer", "Delisle"): lambda x: (60 - x) * 3/2,
        ("Romer", "Newton"): lambda x: (x - 7.5) * 11/40,
        ("Romer", "Reaumur"): lambda x: (x - 7.5) * 16/21,
             }
        
        col1,col2= st.columns([2,2])
        unit= st.text_input("LENGTH", value="0") 
    
        with col1:
         option1 = st.selectbox(
        "FROM",
        [
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Rankine",
            "Delisle",
            "Newton",
            "Reaumur",
            "Romer"
        ]

        )
        with col2:
         option2 = st.selectbox(
        "TO",
                [
            "Fahrenheit",
            "Celsius",
            "Kelvin",
            "Rankine",
            "Delisle",
            "Newton",
            "Reaumur",
            "Romer"
        ]
                )
         
        print('hello')
        
        if (option1, option2) in conversion_factors:
       
         result = conversion_factors[(option1, option2)](float(unit))
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





 
















