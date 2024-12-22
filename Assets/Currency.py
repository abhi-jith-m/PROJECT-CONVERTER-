import streamlit as st

class Currency:
 
  def dCurrency():
      
    conversion_factors = {
    "USD - United States Dollar": 1,
    "EUR - Euro": 0.94,
    "GBP - British Pound Sterling": 0.7848,
    "INR - Indian Rupee": 84.85,
    "JPY - Japanese Yen": 151.4,
    "AUD - Australian Dollar": 1.5635,
    "CAD - Canadian Dollar": 1.417,
    "CNY - Chinese Yuan": 7.25,
    "CHF - Swiss Franc": 0.88,
    "HKD - Hong Kong Dollar": 7.77,
    "SGD - Singapore Dollar": 1.341,
    "NZD - New Zealand Dollar": 1.71,
    "KRW - South Korean Won": 1430.31,
    "ZAR - South African Rand": 17.84,
    "SAR - Saudi Riyal": 3.75,
    "AED - United Arab Emirates Dirham": 3.67,
    "BRL - Brazilian Real": 6.08,
    "MXN - Mexican Peso": 20.25
}

        
         
    col1,col2= st.columns([2,2])
    unit= st.text_input("LENGTH", value="0") 
   
    with col1:
     option1 = st.selectbox(
     "FROM",
     [
    "USD - United States Dollar",
    "EUR - Euro",
    "GBP - British Pound Sterling",
    "INR - Indian Rupee",
    "JPY - Japanese Yen",
    "AUD - Australian Dollar",
    "CAD - Canadian Dollar",
    "CNY - Chinese Yuan",
    "CHF - Swiss Franc",
    "HKD - Hong Kong Dollar",
    "SGD - Singapore Dollar",
    "NZD - New Zealand Dollar",
    "KRW - South Korean Won",
    "ZAR - South African Rand",
    "SAR - Saudi Riyal",
    "AED - United Arab Emirates Dirham",
    "BRL - Brazilian Real",
    "MXN - Mexican Peso"
]
    )
    with col2:
    
     option2 = st.selectbox(
    "TO",
    [
     "EUR - Euro",
    "USD - United States Dollar",
    "GBP - British Pound Sterling",
    "INR - Indian Rupee",
    "JPY - Japanese Yen",
    "AUD - Australian Dollar",
    "CAD - Canadian Dollar",
    "CNY - Chinese Yuan",
    "CHF - Swiss Franc",
    "HKD - Hong Kong Dollar",
    "SGD - Singapore Dollar",
    "NZD - New Zealand Dollar",
    "KRW - South Korean Won",
    "ZAR - South African Rand",
    "SAR - Saudi Riyal",
    "AED - United Arab Emirates Dirham",
    "BRL - Brazilian Real",
    "MXN - Mexican Peso"
]
    )
    print('hello')
    
    value_in_meters = float(unit) / conversion_factors[option1]
    result = value_in_meters * conversion_factors[option2]
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
         