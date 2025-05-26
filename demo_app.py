import streamlit as st
from PIL import Image, ImageDraw

st.title("AI Art Generator Demo")

prompt = st.text_input("Enter your art prompt:")

def generate_placeholder_image(text):
    img = Image.new('RGB', (256, 256), color='white')
    d = ImageDraw.Draw(img)
    d.text((10,120), text[:30], fill=(0,0,0))
    return img

if st.button("Generate"):
    if prompt:
        # Replace this with actual model inference when available
        img = generate_placeholder_image(prompt)
        st.image(img, caption=f"Prompt: {prompt}")
    else:
        st.warning("Please enter a prompt.")
