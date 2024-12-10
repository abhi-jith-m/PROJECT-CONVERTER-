import streamlit as st 

class Display:
  
  def d_volume():
  
    conversion_factors = {
        "Cubic meter": 1,
        "Cubic centimeter": 1e-6,
        "Cubic millimeter": 1e-9,
        "Liter": 0.001,
        "Milliliter": 1e-6,
        "Cubic inch": 0.0000163871,
        "Cubic foot": 0.0283168,
        "Cubic yard": 0.764555,
        "US gallon": 0.00378541,
        "US quart": 0.000946353,
        "US pint": 0.000473176,
        "US cup": 0.000236588,
        "US fluid ounce": 2.9574e-5,
        "US tablespoon": 1.4787e-5,
        "US teaspoon": 4.9289e-6,
        "Imperial gallon": 0.00454609,
        "Imperial quart": 0.00113652,
        "Imperial pint": 0.000568261,
        "Imperial cup": 0.000284131,
        "Imperial fluid ounce": 2.8413e-5,
        "Imperial tablespoon": 1.7758e-5,
        "Imperial teaspoon": 5.9194e-6
    }

 
    
    
    col1,col2= st.columns([2,2])
    unit= st.text_input("LENGTH", value="0") 
   
    with col1:
     option1 = st.selectbox(
     "FROM",
     [
    "Cubic meter",
    "Cubic centimeter",
    "Cubic millimeter",
    "Liter",
    "Milliliter",
    "Cubic inch",
    "Cubic foot",
    "Cubic yard",
    "US gallon",
    "US quart",
    "US pint",
    "US cup",
    "US fluid ounce",
    "US tablespoon",
    "US teaspoon",
    "Imperial gallon",
    "Imperial quart",
    "Imperial pint",
    "Imperial cup",
    "Imperial fluid ounce",
    "Imperial tablespoon",
    "Imperial teaspoon"
]
    )
    with col2:
    
     option2 = st.selectbox(
    "TO",
    [
    "Cubic centimeter",
    "Cubic meter",
    "Cubic millimeter",
    "Liter",
    "Milliliter",
    "Cubic inch",
    "Cubic foot",
    "Cubic yard",
    "US gallon",
    "US quart",
    "US pint",
    "US cup",
    "US fluid ounce",
    "US tablespoon",
    "US teaspoon",
    "Imperial gallon",
    "Imperial quart",
    "Imperial pint",
    "Imperial cup",
    "Imperial fluid ounce",
    "Imperial tablespoon",
    "Imperial teaspoon"
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
         
