# MCP Server

A FastAPI-based MCP (Model Context Protocol) server that exposes tools the backend can call.  
Tools include:
- ping
- system_info
- read_file
- (extendable)

## 🚀 Tech Stack
- Python 3.12
- FastAPI
- Uvicorn
- psutil

## 📁 Folder Structure
mcp-server/
app/
main.py
tools/
ping.py
system_info.py
read_file.py


## ▶️ Running Locally

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start MCP server
uvicorn app.main:app --reload --port=8001

Server runs at:
http://localhost:8001


## 🔌 API Endpoints

### Health Check
GET /health

### Execute Tool
POST /tool
{
"tool_name": "ping",
"args": {}
}


## 🧩 Adding New Tools
Create a new file in:
app/tools/


Example:

```python
def run(args):
    return "hello world"
    
Register it in main.py.