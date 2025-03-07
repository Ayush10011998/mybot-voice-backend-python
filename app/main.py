from fastapi import FastAPI
from app.routers import chatbot, voicebot

app = FastAPI(title="AI Chat & Voice Bot Backend")

# Include chatbot and voice bot routes
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(voicebot.router, prefix="/voicebot", tags=["VoiceBot"])

@app.get("/")
async def root():
    return {"message": "AI Chat & Voice Bot Backend is running!"}