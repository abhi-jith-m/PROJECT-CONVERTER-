import streamlit as st

class Speed:
    
    def dSpeed():
        
        conversion_factors = {
        "Meter per second": 1, 
        "Kilometer per hour": 1000 / 3600,  
        "Miles per hour": 1609.34 / 3600,   
        "Foot per second": 0.3048,         
        "Knot": 1852 / 3600,               
        "Mach": 343,                       
        "Millimeter per second": 0.001,     
        "Lightyear per year": 9.4607e15 / 3.15576e7, 
        "Astronomical unit per day": 1.496e11 / (24 * 3600), 
        "Astronomical unit per hour": 1.496e11 / 3600,  
        "Kilometer per second": 1000,      
        "Mile per second": 1609.34,         
        "Nanometer per second": 1e-9,       
    }

        col1,col2= st.columns([2,2])
        unit= st.text_input("LENGTH", value="0") 
    
        with col1:
         option1 = st.selectbox(
        "FROM",
         [
        "Meter per second",
        "Kilometer per hour",
        "Miles per hour",
        "Foot per second",
        "Knot",
        "Mach",
        "Centimeter per second",
        "Millimeter per second",
        "Lightyear per year",
        "Astronomical unit per day",
        "Astronomical unit per hour",
        "Kilometer per second",
        "Mile per second",
        "Nanometer per second"
        ]

        )
        with col2:
         option2 = st.selectbox(
        "TO",
        [
        "Kilometer per hour",
        "Meter per second",
        "Miles per hour",
        "Foot per second",
        "Knot",
        "Mach",
        "Centimeter per second",
        "Millimeter per second",
        "Lightyear per year",
        "Astronomical unit per day",
        "Astronomical unit per hour",
        "Kilometer per second",
        "Mile per second",
        "Nanometer per second"
        ]
        )
         
        print('hello')
        
        value_in_grams = float(unit) * conversion_factors[option1]
        result = value_in_grams / conversion_factors[option2]
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





 