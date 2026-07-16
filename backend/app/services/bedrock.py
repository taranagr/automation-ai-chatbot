import os
import json
import boto3
from .mcp_client import maybe_call_tools

BEDROCK_REGION = os.getenv("BEDROCK_REGION", "us-east-1")
MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID",
    "anthropic.claude-3-5-sonnet-20240620-v1:0"
)

client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)

async def call_claude(message: str) -> str:
    body = {
        "modelId": MODEL_ID,
        "messages": [{"role": "user", "content": message}],
        "maxTokens": 800,
        "temperature": 0.7
    }

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    # if you wire tool use, intercept here:
    content = result.get("output", {}).get("text") or result.get("content") or ""
    content = await maybe_call_tools(message, content)
    return content
