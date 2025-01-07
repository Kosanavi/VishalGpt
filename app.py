import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

import streamlit as st
from ollama import chat

# Function to interact with the Ollama model and stream the response
def chat_with_ollama(input_text):
    if not input_text:
        return "No input provided."

    # Placeholder for the response
    response_placeholder = st.empty()
    response_content = ""

    # Stream the response from Ollama
    stream = chat(
        model="vishalgpt:latest",
        messages=[{"role": "user", "content": input_text}],
        stream=True,
    )
    for chunk in stream:
        # Append the streamed content to the response
        response_content += chunk["message"]["content"]
        # Update the Streamlit placeholder
        response_placeholder.markdown(response_content)
    
    return response_content

# Streamlit UI
st.title("Chat with VishalGPT")

# Input text box
input_text = st.text_input("Enter your question:")

# Handle user input
if input_text:
    with st.spinner("Writing..."):
        chat_with_ollama(input_text)

