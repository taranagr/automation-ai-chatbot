import subprocess
import json
from app.services.mcp_client import maybe_call_tools
import os

USE_LOCAL_LLM = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"

async def call_local_llm(message: str) -> str:
    if not USE_LOCAL_LLM:
        return message

    # Tool check
    tool_result = await maybe_call_tools(message, message)
    if tool_result != message:
        return tool_result

    # Call Ollama
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", message],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"(local assistant fallback) {message}"
