from e2e1 import *
import streamlit as st

st.title("End to End Encrypter")
user = st.text_input("Enter your message")
st.write(swap_letters(user))