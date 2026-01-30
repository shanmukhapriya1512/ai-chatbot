# AI Chatbot Using LLMs

## Project Objective
Design and implement a full-stack AI chatbot application using modern AI tools and software engineering practices.

## Technologies Used
- **Backend:** FastAPI, Python, OpenAI API
- **Frontend:** Streamlit, Python, Requests
- **Version Control:** GitHub
- **Other Libraries:** python-dotenv, uvicorn

## System Architecture


### Flow:
1. User types a message in the Streamlit frontend.
2. Frontend sends the message to FastAPI backend via HTTP POST.
3. Backend calls OpenAI LLM API using the API key stored in `.env`.
4. Response is returned to frontend and displayed to the user.

## Project Structure

## Setup & Installation

### 1. Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

cd frontend
pip install -r requirements.txt
streamlit run app.py

Including this ensures **anyone can run your project** without asking you questions — it’s a critical part of submission.  

If you want, I can **now give a final version of your README ready to copy-paste completely**, with all sections including Setup, Notes, and Project Structure.