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

    prompt_part = [f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords {keywords}.  Make sure to incorporate these words in the blog. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout"]
#     chat_session = model.start_chat(
#                     history=[
#                         {
#                         "role": "user",
#                         "parts": [
#                             f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords {keywords}.  Make sure to incorporate these words in the blog. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout",
#                         ],
#                         },
#                         {
#                         "role": "model",
#                         "parts": [
#                             "## Philosophy and Religion: Exploring the Complex Interplay\n\nThe relationship between philosophy and religion is as intricate as it is ancient. Throughout history, these two disciplines have engaged in a dynamic dialogue, influencing and shaping each other's perspectives. This blog post will delve into the fascinating intersection of philosophy and religion, examining the concepts of objective morality, the chicken or egg dilemma, the Freudian view, and the hereafter.\n\n### Objective Morality\n\nOne of the central debates in philosophy is the question of whether morality is objective or subjective. Objective morality holds that there are universal moral truths that exist independently of human beliefs or preferences. Religion often plays a key role in advancing objective moral doctrines, as it claims to reveal divine laws or commandments that govern human behavior.\n\n### The Chicken or Egg Dilemma\n\nThe chicken or egg dilemma is a philosophical conundrum that asks which came first: the chicken or the egg? This question has both biological and philosophical implications. In the context of philosophy and religion, it can be applied to the question of whether God created the world or the world existed before God.\n\n### The Freudian View\n\nSigmund Freud's psychoanalytic theories have significantly influenced both philosophy and religion. Freud argued that the human psyche is driven by unconscious forces, including sexual desires, aggression, and a fear of death. His insights have challenged religious beliefs about the nature of the human soul and the afterlife.\n\n### The Hereafter\n\nThe question of what happens after death has preoccupied humanity for centuries. Philosophy and religion offer a variety of perspectives on the hereafter, from the Christian belief in heaven and hell to the Buddhist notion of reincarnation. These beliefs shape our understanding of the meaning and purpose of life.\n\n### Conclusion\n\nThe relationship between philosophy and religion is a complex and ever-evolving one. While these disciplines may differ in their methods and claims, they share a common pursuit of truth and understanding. The concepts of objective morality, the chicken or egg dilemma, the Freudian view, and the hereafter are just a few examples of the many ways in which philosophy and religion engage with profound questions about human existence.\n\nBy exploring these intersections, we can gain a deeper appreciation for the richness and diversity of human thought and the enduring significance of both philosophy and religion in shaping our lives.",
#                         ],
#                         },
#                     ]
# )
    
    response = model.generate_content(prompt_part)

    # print(response.text)

    #creating the submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    st.write(response.text)