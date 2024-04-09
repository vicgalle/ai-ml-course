import streamlit as st
from openai import OpenAI
import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key",
        key="chatbot_api_key",
        value="sk-...",
    )

    os.environ["OPENAI_API_KEY"] = openai_api_key


st.title("Chat with a document")

# upload a document file here
uploaded_file = st.file_uploader("Choose a document file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # save the uploaded file into a file
    with open("data/" + uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getvalue())

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Write your query about the document..."},
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # query
    response = query_engine.query(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response.response)


# Execise 1: modify the previous code to allow for several submitted files at the same time.
