import streamlit as st 

class Display:
  
  def display():
  
    conversion_factors = {
        "Meter": 1, 
        "Kilometer": 1e3,
        "Decimeter": 0.1,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
        "Mile": 1609.34,
        "Fathom": 1.8288,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Inch": 0.0254,
        "Microinch": 2.54e-8, 
    }

 
    
    
    col1,col2= st.columns([2,2])
    unit= st.text_input("LENGTH", value="0") 
   
    with col1:
     option1 = st.selectbox(
     "FROM",
     ["Mile","Foot","Yard","Inch","Meter","Millimeter",
      "Centimeter","Kilometer",'Decimeter','Nanometer','Fathom',
      'Microinch'
      
      ]
    )
    with col2:
    
     option2 = st.selectbox(
    "TO",
    ["Kilometer","Foot","Yard","Inch","Meter","Millimeter",
      "Centimeter","Mile",'Decimeter','Nanometer','Fathom',
      'Microinch'
      
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
         
