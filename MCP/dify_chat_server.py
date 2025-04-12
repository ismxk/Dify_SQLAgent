# dify_server.py
from mcp.server.fastmcp import FastMCP
import requests
import json

# 创建MCP服务器
mcp = FastMCP("Dify_chat")

# Dify API配置
DIFY_API_KEY = "app-zaQzeSJb334hVUjfmKLg1DIy"
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

@mcp.tool()
def query_dify_chat(prompt: str) -> str:
    """
    使用聊天机器人，从标题生成报告
    """
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": {},
        "query": prompt,
        "user": "test_user",
        "stream": False
    }
    
    try:
        response = requests.post(DIFY_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result.get("answer", "无法获取回答")
    except Exception as e:
        return f"请求Dify API时出错: {str(e)}"

# 启动服务器
if __name__ == "__main__":
    print("启动 Dify MCP 服务器...")
    mcp.run() 