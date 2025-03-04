import streamlit as st
import pandas as pd

st.title("🐷🐷🐷Website Developing using Python🐷🐷")
st.header("🍖🍖Website Developing using Python🍖🍖")

st.image('./img/hq720.jpg')
st.subheader("Aingkarat boonpleng")
col1,col2,col3 = st.columns(3)

with col1 :
    st.header("versicolor")
    st.image("./img/iris1.png")
with col2 :
    st.header("Virginica")
    st.image("./img/iris2.jpg")
with col3 :
    st.header("Setosa")
    st.image("./img/iri3.jpg")

html = """
<div style="background-color:#4ad72d;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5> flower </h5></center>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
st.markdown("")
st.subheader("ส่วนแรก 10")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))
st.subheader("ส่วนท้าย 10")
st.write(dt.tail(10))