import streamlit as st
class Number:
    def d_number():
        bases={
            "Binary": 2,
            "Decimal": 10,
            "Octal": 8,
            "Hexadecimal": 16
        }
        
        col1,col2= st.columns([2,2])
        unit= st.text_input("LENGTH", value="0")
        with col1:
            option1=st.selectbox(
                "FROM",
                    [
                       "Binary",
                       "Decimal",
                       "Octal",
                       "Hexadecimal",
                    ]
            )
        with col2:
            option2=st.selectbox(
                "TO",
                [
                    "Decimal",
                    "Binary",
                    "Hexadecimal",
                    "Octal"
                ]
            )
            
        
        try:
            decimal_value = int(unit, bases[option1])
    
            if option2 == "Binary":
                result= bin(decimal_value)[2:]
            elif option2  == "Decimal":
                result= str(decimal_value)
            elif option2  == "Octal":
                result=oct(decimal_value)[2:]
            elif option2  == "Hexadecimal":
                result = hex(decimal_value)[2:].upper()
                
        except ValueError:
            st.error("Invalid input for the selected base!")
            
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