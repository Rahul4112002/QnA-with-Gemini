import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    temperature=0,
)

prompt = ChatPromptTemplate(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)

st.title("QnA with Gemini")
input_text = st.text_input("Enter your question here")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))