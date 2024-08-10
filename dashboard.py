import streamlit as st
import os
from PIL import Image

def display_screenshots():
    st.title("Screenshots")
    screenshot_files = [f for f in os.listdir('logs') if f.endswith('.png')]
    for screenshot in screenshot_files:
        img = Image.open(f'logs/{screenshot}')
        st.image(img, caption=screenshot)

if __name__ == "__main__":
    display_screenshots()
