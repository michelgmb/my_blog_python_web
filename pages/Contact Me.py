import streamlit as st
from PIL import Image
image = Image.open('images/photogmb.png')

st.image(image, caption='Sunrise by the mountains')