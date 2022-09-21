import streamlit as st
from PIL import Image

st.title('アプリ')

uploaded_file = st.file_uploader('CHoose an image...',type='jpg',accept_multiple_files=True)

if uploaded_file is not None:
    for i in uploaded_file:
        if st.checkbox(i.name):
            img = Image.open(i)
            # st.image(img,caption='Uploaded Image.',use_column_width=True)
            st.image(img,caption=i.name,use_column_width=True)
