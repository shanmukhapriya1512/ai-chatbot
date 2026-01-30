import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.title("AI Chatbot")

user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input:
        try:
            response = requests.post(API_URL, json={"message": user_input})
            data = response.json()
            st.success(f"AI: {data['response']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")