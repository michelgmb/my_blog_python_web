import streamlit as st

st.title("Home")

col1, col2 = st.columns(2)
with col1:
       col1 = st.image('images/photogmb.png' ),
with col2:
     col2 = st.write(""" This post is about my achievement .My Passion for coding,
                     in python my Careers as a devops engineer.
                     All the glory must be to God !""")
