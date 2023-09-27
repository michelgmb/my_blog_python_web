import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Home")

col1, col2 = st.columns(2)
with col1:
    col1 = st.image('images/photogmb.png'),
with col2:
    col2 = st.subheader('Michel Gandeu')
    content1 = """ 
    This post is about my achievement .My Passion for coding,
    in python my Careers as a devops engineer.
    All the glory must be to God !
    """
    st.info(content1)

content2 = "Below you can find some of the apps i have built in python. Feel free to contact me!"

col3 = st.write(content2)

col4, col5, col6 = st.columns([0.45, 0.10, 0.45])
df = pd.read_csv('data.csv', sep=';')

with col4:
    for col, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col6:
    for col, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
