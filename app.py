import streamlit as st

import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

# Creating the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = We could Adjust safety settings if we want
)


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
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    #creating the submit button
    submit_button = st.button("Generate Blog")

    #constructing the prompt
    prompt_part = [f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords {keywords}.  Make sure to incorporate these words in the blog. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout"]
    
    #getting the model responce
    response = model.generate_content(prompt_part)
    

if submit_button:
    st.write(response.text)