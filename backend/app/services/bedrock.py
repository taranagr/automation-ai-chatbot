# backend/app/services/bedrock.py

import json
from app.services.mcp_client import maybe_call_tools

async def call_claude(message: str) -> str:
    """
    Local-only mode:
    - No AWS
    - No Bedrock
    - Simulates Claude behavior
    - Supports MCP tool calls
    """

    # If the user triggers a tool call, run it
    tool_result = await maybe_call_tools(message, message)
    if tool_result != message:
        return tool_result

    # Otherwise, simulate a simple assistant response
    return f"(local assistant) You said: {message}"
