from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat

app = FastAPI(title="AI Chatbot Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
