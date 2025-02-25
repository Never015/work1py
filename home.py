import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./img/21792.jpg')
st.subheader("Aingkarat boonpleng")
col1,col2,col3 = st.columns(3)

with col1 :
    st.header("skrim")
    st.image("./img/skyrim.png")
with col2 :
    st.header("cat1")
    st.image("./img/cat.jpg")
with col3 :
    st.header("bcat")
    st.image("./img/hq720.jpg")

html = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
st.markdown("")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))