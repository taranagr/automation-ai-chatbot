import boto3
import json
from app.services.mcp_client import maybe_call_tools

# Claude model ID
MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"

# Create Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

async def call_claude(message: str) -> str:
    """
    Claude via AWS Bedrock.
    Supports MCP tool calls.
    Falls back to local-only mode if AWS credentials are missing.
    """

    # 1. Tool call check
    tool_result = await maybe_call_tools(message, message)
    if tool_result != message:
        return tool_result

    # 2. Claude request
    try:
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [
                {"role": "user", "content": message}
            ]
        }

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(payload)
        )

        body = json.loads(response["body"].read())
        return body["content"][0]["text"]

    except Exception as e:
        # Fallback to local-only mode
        return f"(local assistant fallback) {message}"
