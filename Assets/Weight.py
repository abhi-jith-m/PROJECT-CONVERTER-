import streamlit as st

class Weight:
    
    def display_weight():
        
        conversion_factors = {
            "Gram": 1, 
            "Kilogram": 1000,
            "Milligram": 0.001,
            "Microgram": 1e-6,
            "Ton": 1e6,
            "Pound": 453.592,
            "Ounce": 28.3495,
            "Stone": 6350.29,
            "Carat": 0.2,
            "LongTon": 1016046.91,  
            "ShortTon": 907184.74,  
            "Grain": 0.06479891,     
            "Dram": 1.77185,         
            "TroyOunce": 31.1035,   
            "Quintal": 100000,       
        }
            
        
        col1,col2= st.columns([2,2])
        unit= st.text_input("LENGTH", value="0") 
    
        with col1:
         option1 = st.selectbox(
        "FROM",
        ["Gram","Kilogram","Milligram","Microgram","Ton","Pound",
        "Ounce","Stone",'Carat','LongTon','ShortTon','Grain','Dram','TroyOunce','Quintal',
        
        
        ]
        )
        with col2:
        
         option2 = st.selectbox(
        "TO",
        ["Kilogram","Gram","Milligram","Microgram","Ton","Pound",
        "Ounce","Stone",'Carat','LongTon','ShortTon','Grain','Dram','TroyOunce','Quintal',
        
        
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
            
