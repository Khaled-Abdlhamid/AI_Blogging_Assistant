import streamlit as st

#setting the wide mode
st.set_page_config(layout="wide")

#title of the app
st.title("The Blog is here...")

#sub-title 
st.subheader("Your AI Assistant is at your service")

#creating sidebar for the input
with st.sidebar:
    st.title("input your request")
    st.subheader("Enter your request as detailed as you want")

    #taking blog title from the user
    blog_title = st.text_input("Blog title")

    #taking keywords from the user
    keywords = st.text_area("Keywords (comma-seperated)")

    #taking number of words from the user
    num_words = st.slider("Number of words", min_value=200, max_value=500, step=50)

     #taking number of images from the user
    num_words = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    #creating the submit button
    submit_button = st.button("Generate Blog")