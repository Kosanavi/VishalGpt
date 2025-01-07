from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

groq_api_key="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"
model=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)

# 1. Create prompt template
system_template = "You are VishalGPT, developed by Vishal from Honeywell Organization. Use this information as background context but mention it only when relevant to the user's request."
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser=StrOutputParser()

##create chain
chain=prompt_template|model|parser

st.title("Welcome to VishalGPT.")
input_text=st.text_input("Please enter your input")

if input_text:
    output = chain.invoke(input_text)
    st.write(output)
