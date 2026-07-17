import os
import httpx

MCP_SERVER_URL = "http://localhost:8001"
# MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")  # e.g. http://mcp.internal:8001

async def maybe_call_tools(message: str, fallback: str) -> str:
    if message.startswith("[tool:"):
        tool_name = message.replace("[tool:", "").replace("]", "")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{MCP_SERVER_URL}/tool",
                    json={"tool_name": tool_name, "args": {}}
                )
            return response.json().get("result", "Tool execution failed")
        except Exception as e:
            return f"Tool error: {str(e)}"
    return fallback
