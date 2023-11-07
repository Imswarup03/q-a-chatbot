# Q&A chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()  # take all the env variables from the .env file
import streamlit as st
import os

# function to load OpenAI model and get responses

openai_api_key=os.environ.get("OPENAI_API_KEY")

def get_openai_response(user_input):
    llm= OpenAI(model_name="text-davinci-003",temperature=0.5)
    response=llm(user_input)
    return response

input = st.text_input("Ask me a anything:",key="input")

# initialize streamlit app
st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot:")

st.header("Q&A Chatbot")

response = get_openai_response(input)

submit = st.button("Submit")

if submit:
    st.subheader("Answer")
    st.write(response)

