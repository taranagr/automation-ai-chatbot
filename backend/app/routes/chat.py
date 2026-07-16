from fastapi import APIRouter
from pydantic import BaseModel
from ..services.bedrock import call_claude

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    role: str
    content: str

@router.post("", response_model=ChatResponse)
async def chat(req: ChatRequest):
    content = await call_claude(req.message)
    return ChatResponse(role="assistant", content=content)
