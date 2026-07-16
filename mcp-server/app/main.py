from fastapi import FastAPI
from pydantic import BaseModel
import importlib
import pkgutil
from app.tools import __path__ as tools_path

app = FastAPI(title="MCP Server")

# -----------------------------
# Tool Registry
# -----------------------------
TOOLS = {}

def load_tools():
    """Dynamically load all tools in app/tools."""
    for module in pkgutil.iter_modules(tools_path):
        mod = importlib.import_module(f"app.tools.{module.name}")
        if hasattr(mod, "register"):
            tool_name, func = mod.register()
            TOOLS[tool_name] = func

load_tools()

# -----------------------------
# Request/Response Models
# -----------------------------
class ToolRequest(BaseModel):
    tool_name: str
    args: dict | None = None

class ToolResponse(BaseModel):
    result: str

# -----------------------------
# Routes
# -----------------------------
@app.post("/tool", response_model=ToolResponse)
async def tool(req: ToolRequest):
    if req.tool_name not in TOOLS:
        return ToolResponse(result=f"Unknown tool: {req.tool_name}")

    func = TOOLS[req.tool_name]
    result = func(req.args or {})
    return ToolResponse(result=result)

@app.get("/health")
async def health():
    return {"status": "ok", "tools": list(TOOLS.keys())}

