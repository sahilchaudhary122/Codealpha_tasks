import fastapi  # type: ignore[import]
from chatbot import get_response

app = fastapi.FastAPI()

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