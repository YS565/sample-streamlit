import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import yolov5
import cv2

path = 'yolov5s.pt'
# my_conf = 0
# my_iou = 0

st.title("WebCam yolov5 Inference")

my_conf = st.slider('確信度', min_value=0, max_value=100)
my_iou = st.slider('IOU', min_value=0, max_value=100)

model = yolov5.load(path,device='cpu')

model.conf,model.iou = my_conf/100,my_iou/100


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
