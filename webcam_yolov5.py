import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import yolov5 as y5
import cv2

path = 'C:/Users/koji/Desktop/Work/yolov5/yolov5s.pt'

model = y5.load(path,device='cpu')

st.title("WebCam yolov5 Inference")

def callback(frame):
    img = frame.to_ndarray(format="rgb24")

    result = model(img,size=img.shape[0])
    result.render()
    img_result = result.ims[0]

    img_result = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)

    return av.VideoFrame.from_ndarray(img_result,format="bgr24")

webrtc_streamer(
    key="example",
    video_frame_callback=callback,
    rtc_configuration={  # この設定を足す
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)
