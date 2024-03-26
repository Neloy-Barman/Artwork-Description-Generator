import streamlit as st

st.title(body="Artwork Caption Generator")

col_left, col_right = st.columns(2)

with col_left:
    col11, col12 = st.columns(2)
    with col11:
        st.image(image="streamlit\\assets\drawing.jpeg")
    with col12:
        st.write("<div style='text-align:right;'>Witness the birth of creativity. Our website breathes life into your artistic visions.</div>", unsafe_allow_html=True)
    col21, col22 = st.columns(2)
    with col21:
        st.write("<div style='text-align:left;'>Delve into the depths of inspiration. Explore our platform to give voice to your masterpiece.</div>", unsafe_allow_html=True)
    with col22:
        st.image(image="streamlit\\assets\\thinking.jpeg")
    col31, col32 = st.columns(2)
    with col31:
        st.image(image="streamlit\\assets\generate.jpeg")
    with col32:
        st.write("<div style='text-align:right;'>Crafting the narrative of your creation. Unleash your imagination with our caption generator for artwork.</div>", unsafe_allow_html=True)
    

with col_right:
    image = st.file_uploader(accept_multiple_files=False, label='Upload an Image')

    if image is not None:
        print(image)
        st.image(image=image, caption='Uploaded Image', width=200)
        # st.write(f'<div style="display: flex; justify-content: center;"><img src="{image}" /></div>', unsafe_allow_html=True)

        if st.button(label='Submit'):
            st.success('Image processed successfully!!')