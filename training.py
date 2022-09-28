#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
from PIL import Image


# In[7]:


#ワイド表示
st.set_page_config(layout="wide")

#セレクトボックスのリストを作成
page_list = ["page1","page2"]

#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択",page_list)

if selector=="page1":
    password = st.text_input('社員番号')
    if password=='126537':
        st.title("ページ1のタイトル")
elif selector=="page2":
    if st.button('ページ2ボタン'):
        st.title("ページ2のタイトル")

