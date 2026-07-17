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

## 🧩 Use Claude via Anthropic API
###  Sign up for Anthropic
Go to Anthropic Console
Create an account (or log in if you already have one)

###  Get your API key
In the Anthropic Console, navigate to API Keys
Click Create Key
Copy the key (looks like sk-ant-xxxxxxxxxxxxxxxx)
⚠️ Keep this secret — it’s like a password.

###  Install Anthropic Python SDK
pip install anthropic

### Set Your API Key
setx ANTHROPIC_API_KEY "sk-ant-xxxxxxxxxxxxxxxx"
Restart your terminal so the environment variable is available.

## 🧩 Use Claude Call via AWS Bedrock (No Local-Only Mode)
### Download and Install AWS CLI
Go to the official AWS page:
AWS CLI for Windows (MSI Installer)
Choose the latest AWS CLI v2 MSI installer for Windows.

### Use AWS credentials
You must create an IAM user or role with Bedrock permissions.
Generate Access Key ID and Secret Access Key.
Configure them locally (aws configure or environment variables).

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

##  🧩 Use Open-Source LLMs
You can integrate an open‑source LLM locally instead of relying on AWS or Anthropic. This gives you full control, offline capability, and avoids API costs.

### Open Source LLMs
LLaMA 3 → Meta’s latest model, widely used, strong performance.
Mistral → Lightweight, efficient, great for local inference.
GPT‑J / GPT‑NeoX → Older but still capable, easy to run.
Ollama → A tool that makes running models locally very simple.

### Install Ollama (easiest path)
Download and Install Ollama: ollama.ai
Run a model, e.g. LLaMA 3:
PS Command: ollama run llama3
### Integrate with your backend
Modify your bedrock.py (or create local_llm.py) to call Ollama:


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
