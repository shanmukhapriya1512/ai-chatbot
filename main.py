from fastapi import FastAPI
from pydantic import BaseModel
from llm import get_llm_response

app = FastAPI(title="AI Chatbot Backend")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        reply = get_llm_response(request.message)
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}