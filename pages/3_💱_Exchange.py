import streamlit as st
from currency_converter import CurrencyConverter

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.markdown("""
In this currency converter you'll be asked to enter the amount of money you'd like to convert, the coin shortcut you'd
 like to convert from and the same for the coin you'd like to convert to. You
 For example, to convert 10 euro into USD you'd need to fill
 
  `Amount: 10`
  
  `From: EUR`
  
  `To: USD`
""")

c = CurrencyConverter()
converted = 0

form = st.form("Money Converter")
form.title("Money Converter")
amt = form.number_input("Amount", value=0.00)
from_coin = form.text_input("From").upper()
to_coin = form.text_input("To", value="USD").upper()
result = form.text_input("Result", value=f"{c.convert(amt, from_coin, to_coin):.3f} {to_coin}", disabled=True)
submit_button = form.form_submit_button()
if submit_button:
    try:
        converted = c.convert(amt, from_coin, to_coin)

    except Exception as e:
        form.error(e)