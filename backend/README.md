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

## 🧩 AWS Mode > Claude Call (No Local-Only Mode)
### Set aws credentials in Powershell
setx AWS_ACCESS_KEY_ID "YOUR_KEY"
setx AWS_SECRET_ACCESS_KEY "YOUR_SECRET"
setx AWS_REGION "us-east-1"

or 

Create
C:\Users\<you>\.aws\credentials
And Add
[default]
aws_access_key_id=YOUR_KEY
aws_secret_access_key=YOUR_SECRET
region=us-east-1

### Verify credentials
aws sts get-caller-identity

### Get temporary credentials via AWS CLI
aws sts get-session-token --duration-seconds 3600

Set in Powershell
setx AWS_ACCESS_KEY_ID "ASIAxxxxxxxxxxxx"
setx AWS_SECRET_ACCESS_KEY "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
setx AWS_SESSION_TOKEN "IQoJb3JpZ2luX2VjE..."
setx AWS_REGION "us-east-1"

## 🔌 API Endpoints

### Health Check
GET /health

Invoke-RestMethod -Uri "http://localhost:8001/health" -Method GET

{ "status": "ok" }

### Chat
POST /chat
{
"message": "hello"
}

Invoke-RestMethod -Uri "http://localhost:8000/chat" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"message": "hello"}'

{ "result": "(local assistant) You said: hello" }


### MCP Tool Call
POST /chat
{
"message": "[tool:ping]"
}

Invoke-RestMethod -Uri "http://localhost:8000/chat" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"message": "[tool:ping]"}'

{ "result": "pong" } 

This ensures [tool:ping] → MCP server → "pong"

Invoke-RestMethod -Uri "http://localhost:8001/tool" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"tool_name": "ping", "args": {}}'

{ "result": "pong" } 


## 📚 Related Docs
- **[Frontend README](ca://s?q=Show_frontend_README)**  
- **[MCP Server README](ca://s?q=Show_MCP_server_README)**  
