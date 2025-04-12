import subprocess
# dify_server.py
from mcp.server.fastmcp import FastMCP
import requests
import json

# 创建MCP服务器
mcp = FastMCP("Dify_agent")

# Dify API配置
DIFY_API_KEY = "app-mGVmL8qyi10giSPJhKayTAg9"
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

@mcp.tool()
def query_dify_agent(prompt: str) -> str: 
    """
    使用更强的agent，从标题生成报告
    """
    # 构造 curl 命令
    curl_command = [
        "curl", "-X", "POST", DIFY_API_URL,
        "-H", f"Authorization: Bearer {DIFY_API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", f'{{"inputs": "", "query": "{prompt}", "user": "test_user", "response_mode": "streaming"}}'
    ]
    
    try:
        # 使用 subprocess 运行 curl 命令
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        
        # 打印命令输出
        print("API响应:")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"请求 Dify API 时出错: {str(e)}")
        print(f"错误输出: {e.stderr}")

if __name__ == "__main__":
    print("启动 MCP Dify_agent 服务器...")
    mcp.run()
