import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers


# function to get response from Llama2 model
def getLlamaresponce(input_text, no_words, blog_style):

    #calling our Llama2 model
    llm = ctransformers.CTransformers(model='C:/Users/LENOVO/DS/LLM/Blog using Llama2/Models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens':256, 'temperature':0.01})
    
    #prompt template
    template = '''
                write a blog for {blog_style} for a topic {input_text} within {no_words} words
                '''
    
    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_words'],
                            template=template)
    
    #generating the responce
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)

    return response




st.set_page_config(page_title="Blog Gnerator", 
                   layout='centered', 
                   initial_sidebar_state='collapsed')

st.header('Generate Blogs :)')

input_text = st.text_input('Enter the blog topic')

#creating two additional columns for nummer of words and target audiance
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('Number of words')

with col2:
    blog_style = st.selectbox("Writing the blog for", 
                              ('Researchers', 'Data Scientists', "Common Man"), index=0)
    
submit = st.button("Generate")

if submit:
    st.write(getLlamaresponce(input_text, no_words, blog_style))
