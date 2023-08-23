import streamlit as st
from rembg import remove

from PIL import Image

def main():
    st.title("Alpha Matting")
    uploaded_files = st.file_uploader("Upload an image")
    if st.button("Generate"):
        if uploaded_files:
            img = Image.open(uploaded_file)
            res = bg_remove(img)
            col1, col2 = st.columns(2,gap='wide')
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)
            st.image(res)
        
        else:
            st.error("Please upload an image")

def bg_remove(image):
    return remove(image)

if __name__=="__main__":
    main()