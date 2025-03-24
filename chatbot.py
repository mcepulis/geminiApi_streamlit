from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("Chat with Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.container():
    st.subheader("Chat History")
    if not st.session_state.messages:
        st.info("No messages yet. Start the conversation!")
    else:
        for message in st.session_state.messages:
            with st.expander(f"{message['role'].capitalize()} says:"):
                st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=[
                {"role": m["role"], "parts": [{"text": m["content"]}]}  
                for m in st.session_state.messages
            ]
        )
        st.markdown(response.text) 
    st.session_state.messages.append({"role": "assistant", "content": response.text})