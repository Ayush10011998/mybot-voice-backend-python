from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/message")
async def chatbot_response(chat_request: ChatRequest):
    user_message = chat_request.message
    bot_response = f"AI Bot: You said '{user_message}'"
    return {"response": bot_response}