import streamlit as st
from PIL import Image

st.header('your email address')
with st.form(key="email_form"):
    user_email = st.text_input('Your email address')
    message = st.text_area("your message") # for multiline text input
    button = st.form_submit_button(label='summit')

    if button :
        print('hello')