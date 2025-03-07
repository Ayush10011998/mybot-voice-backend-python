from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_voicebot():
    return {"message": "Voice bot API is working!"}