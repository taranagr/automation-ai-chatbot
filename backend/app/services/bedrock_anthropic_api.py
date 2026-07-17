import os
from anthropic import Anthropic
from app.services.mcp_client import maybe_call_tools

# Load API key from environment variable
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=ANTHROPIC_API_KEY)

async def call_claude(message: str) -> str:
    """
    Claude via Anthropic API.
    Supports MCP tool calls.
    """

    # 1. Tool call check
    tool_result = await maybe_call_tools(message, message)
    if tool_result != message:
        return tool_result

    # 2. Claude request
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1024,
            messages=[{"role": "user", "content": message}]
        )
        return response.content[0].text
    except Exception as e:
        return f"(local assistant fallback) {message}"
