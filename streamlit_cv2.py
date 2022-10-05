#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("My first Streamlit app")
st.write("Hello, world")

webrtc_streamer(
    key="example",
    video_frame_callback=callback,
    rtc_configuration={  # この設定を足す
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)

# In[ ]:




