# AI Chatbot System

A full‑stack AI workspace consisting of a Next.js frontend, a FastAPI backend, and a FastAPI‑based MCP server.  
The system supports chat interactions, tool execution, and workspace modules such as Agent, Tests, and Tools.

---

## 🌐 System Architecture

The project is composed of three services:

### 1. Frontend (Next.js + TypeScript)
- Provides the UI and navigation
- Communicates with backend via REST API
- Runs at: http://localhost:3000

### 2. Backend (FastAPI + Python)
- Processes chat messages
- Executes MCP tools
- Supports local‑only mode (no AWS required)
- Runs at: http://localhost:8000

### 3. MCP Server (FastAPI + Python)
- Exposes tools such as `ping`, `system_info`, `read_file`
- Runs at: http://localhost:8001

---

## 📁 Repository Structure
ai-chatbot/
frontend/      # Next.js UI
backend/       # FastAPI backend
mcp-server/    # MCP tool server


Each folder contains its own README:

- [Frontend README](ca://s?q=Show_frontend_README)
- [Backend README](ca://s?q=Show_backend_README)
- [MCP Server README](ca://s?q=Show_MCP_server_README)

---

## ▶️ Running the Entire System Locally

### Frontend Setup
1. Download and Install NodeJS from nodejs.org
2. Install npm
    cd C:\automation-ai-chatbot\frontend
    npm install
3. Validate by running command node -v or npm -v in powershell
### Backend Setup
4. pip install requirements for backend
    cd C:\automation-ai-chatbot\backend
    pip install -r requirements.txt
### MCP-SERVER Setup
5. pip install requirements for mcp-server
    cd C:\automation-ai-chatbot\mcp-server
    pip install -r requirements.txt

### 1. Start the MCP Server
    C:\ChatBot\ai-chatbot\mcp-server
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8001
    output: Uvicorn running on http://127.0.0.1:8001
    validate in browser http://localhost:8001/health

### 2. Start the Backend
    C:\ChatBot\ai-chatbot\backend
    uvicorn app.main:app --reload --port 8000
    output: Uvicorn running on http://127.0.0.1:8000
    validate in browser http://localhost:8000/health

### 3. Start the Frontend
    C:\ChatBot\ai-chatbot\frontend
    npm run dev

Open the UI:
http://localhost:3000/


https://coreui.io/react/docs/components/sidebar/#

Frontend -> Backend -> MCP Tools -> Backend -> Frontend

## 📁 Detailed Repository Structure

├── frontend/          → Next.js + shadcn/ui (Amplify)
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   ├── next.config.mjs
│   └── tailwind.config.ts
│
├── backend/           → FastAPI (Lambda)
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   ├── lambda_handler.py
│   └── pyproject.toml
│
├── mcp-server/        → MCP Tools Server (EC2)
│   ├── app/
│   │   └── main.py
│   └── pyproject.toml
│
└── infra/             → AWS infra stubs (optional)
    ├── amplify/
    ├── lambda/
    └── ec2/


---

## 💬 Chat Flow

1. User sends a message from the frontend  
2. Backend receives `/chat` request  
3. Backend checks if message contains a tool call  
4. If tool call → backend forwards to MCP server  
5. MCP server executes tool and returns result  
6. Backend returns final response to frontend  

Example tool call:


---

## 🧩 Features

### Agent
- Chat interface
- Tool execution

### Tests
- Test Plans
- Test Cases
- Test Sets
- Test Runs

### Tools
- Create Orders (custom tool integration)

---

## 🛠 Adding New MCP Tools

1. Create a new file in:
mcp-server/app/tools/


2. Implement a `run(args)` function
3. Register the tool in `main.py`
4. Call it from the frontend using:

[tool:your_tool_name]

---

## 🧪 Testing

### Backend Health
GET http://localhost:8000/health
### MCP Server Health
GET http://localhost:8001/health
### Chat Test
POST http://localhost:8000/chat
{
"message": "hello"
}

### Tool Test
POST http://localhost:8000/chat
{
"message": "[tool:ping]"
}


---

## 👥 Developer Notes

- System supports **local‑only mode** (no AWS required)
- Backend and MCP server are fully async
- Frontend uses Next.js App Router
- Sidebar navigation is modular and expandable

---

## 📚 Related Documentation

- [Frontend README](ca://s?q=Show_frontend_README)
- [Backend README](ca://s?q=Show_backend_README)
- [MCP Server README](ca://s?q=Show_MCP_server_README)

