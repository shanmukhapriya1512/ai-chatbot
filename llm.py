import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_llm_response(message: str):
   
    api_key = os.getenv("OPENAI_API_KEY")
    
   
    if not api_key:
        return f"You said: {message}"
    client = OpenAI(api_key=api_key)
    
    return f"You said: {message}"