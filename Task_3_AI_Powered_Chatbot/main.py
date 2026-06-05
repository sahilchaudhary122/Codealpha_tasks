from fastapi import FastAPI

from chatbot import get_response

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Chatbot System"
    }


@app.get("/chat")
def chat(message: str):

    response = get_response(
        message
    )

    return {
        "user_message": message,
        "bot_response": response
    }