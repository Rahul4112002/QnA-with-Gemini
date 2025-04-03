import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0,
)

prompt = ChatPromptTemplate(
    [
        ("system","You are a helpful assistant that translates {input_language} to {output_language}."),
        ("human","{input}")
    ]
)

st.title("Gemini Language Translator")
input_text=st.text_input("Write the sentence in english and it will be translated in german")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser  

if input_text:
    st.write(chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": input_text, 
        #"input": "I love programming.",
    }
))