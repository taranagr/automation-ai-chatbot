1. Download and Install NodeJS from nodejs.org
2. Install npm
    cd C:\automation-ai-chatbot\frontend
    npm install
3. Validate by running node -v or npm -v
4. pip install requirements for backend
    cd C:\automation-ai-chatbot\backend
    pip install -r requirements.txt
5. pip install requirements for mcp-server
    cd C:\automation-ai-chatbot\mcp-server
    pip install -r requirements.txt
6. Start MCP Server
    C:\ChatBot\ai-chatbot\mcp-server
    uvicorn app.main:app --reload --port 8001
    output: Uvicorn running on http://127.0.0.1:8001
    validate in browser http://localhost:8001/health
7. Start Backend Server
    C:\ChatBot\ai-chatbot\backend
    uvicorn app.main:app --reload --port 8000
    output: Uvicorn running on http://127.0.0.1:8000
    validate in browser http://localhost:8000/health
8. Start Frontend Server
    C:\ChatBot\ai-chatbot\frontend
    npm run dev
9. Access frontend UI in browser http://localhost:3000/


https://coreui.io/react/docs/components/sidebar/#

Frontend -> Backend -> MCP Tools -> Backend -> Frontend

Repo Structure

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