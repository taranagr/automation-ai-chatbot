import os
import httpx

MCP_URL = os.getenv("MCP_SERVER_URL")  # e.g. http://mcp.internal:8001

async def maybe_call_tools(user_message: str, model_output: str) -> str:
    # Stub: in a real setup, parse tool calls from model_output
    # and call MCP server. For now, just return model_output.
    # Example:
    # async with httpx.AsyncClient() as client:
    #     res = await client.post(f"{MCP_URL}/tool", json={...})
    #     tool_result = res.json()
    #     ...
    return model_output
