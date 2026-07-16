# AI Chatbot Frontend

A modern React + Next.js interface for interacting with the AI Chatbot backend and MCP server.  
Provides navigation, chat UI, and workspace tools.

## 🚀 Tech Stack
- TypeScript
- Next.js (App Router)
- React
- Tailwind CSS
- Axios (API communication)

## 📁 Folder Structure
frontend/
app/
components/
lib/
public/
styles/

## 🔧 Environment Variables
Create `.env.local`:
NEXT_PUBLIC_API_URL=http://localhost:8000

## ▶️ Running Locally
Install dependencies:
npm install

## Start development server:
npm run dev

## Open the UI:
http://localhost:3000

## 🧩 Features
- Sidebar navigation (Agent, Tests, Tools)
- Chat interface
- Tool execution UI
- Workspace pages (Test Plans, Test Cases, Test Sets, Test Runs)

## 🔌 API Communication
The frontend communicates with the backend via:
POST /chat


Backend URL is defined by `NEXT_PUBLIC_API_URL`.

## 📚 Related Docs
- **[Backend README](ca://s?q=Show_backend_README)**  
- **[MCP Server README](ca://s?q=Show_MCP_server_README)**  
