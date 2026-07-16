# AI Chatbot Backend

A FastAPI backend that connects the frontend UI to the MCP server and (optionally) Claude via AWS Bedrock.  
Supports full **local-only mode**, meaning no AWS credentials are required.

## 🚀 Tech Stack
- Python 3.12
- FastAPI
- Uvicorn
- httpx
- Optional: AWS Bedrock (Claude)

## 📁 Folder Structure
backend/
app/
main.py
services/
bedrock.py
mcp_client.py


## ▶️ Running Locally

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start backend
uvicorn app.main:app --reload --port 8000

Backend runs at:
http://localhost:8000

## 🔧 Environment Variables
MCP_SERVER_URL=http://localhost:8001


## 🧩 Local-Only Mode (No AWS Required)
The backend is configured to run offline using a simple local LLM simulator.  
This means:
- No AWS credentials needed  
- No Bedrock calls  
- MCP tools still work  
- Chat responses come from a local function  

## 🔌 API Endpoints

### Health Check
GET /health

### Chat
POST /chat
{
"message": "hello"
}

### MCP Tool Call
POST /chat
{
"message": "[tool:ping]"
}


## 📚 Related Docs
- **[Frontend README](ca://s?q=Show_frontend_README)**  
- **[MCP Server README](ca://s?q=Show_MCP_server_README)**  
