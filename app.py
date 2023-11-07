# Q&A chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()  # take all the env variables from the .env file
import streamlit as st
from langchain.chat_models import ChatOpenAI
import os

# function to load OpenAI model and get responses

openai_api_key=os.environ["OPENAI_API_KEY"]

def get_openai_response(user_input:str):
    llm= OpenAI(model_name="gpt-3.5-turbo",temperature=0.5)
    response=llm(user_input)
    if response:
        return response

st.set_page_config(page_title="Q&A Chatbot", page_icon=":robot", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.header("Q&A Chatbot")


user_input = st.chat_input("Ask me a anything:")

# submit = st.button("Submit")
print("user:",user_input)


if user_input!=None:
    st.write("user:",user_input)
    response = get_openai_response(user_input)



if user_input and response:
    with st.chat_message("user:"):
        # st.write(input)
        st.write("Lucy:",response)
        
