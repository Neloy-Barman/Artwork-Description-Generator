import streamlit as st

st.title(body="Hello world")

container = st.container()
with container:
    col_left, col_right = st.columns(2)

    with col_left:
        col11, col12 = st.columns(2)
        with col11:
            st.image(image="itl_1593.jpg")
        with col12:
            st.subheader(body="Hello world")
        col21, col22 = st.columns(2)
        with col21:
            st.title(body="Hello world")
        with col22:
            st.image(image="itl_1593.jpg")
        col21, col22 = st.columns(2)
    
    