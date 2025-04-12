# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("求余数")

# Add an addition tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """求a除以b的余数"""
    return a % b

# 启动服务器
if __name__ == "__main__":
    print("启动 MCP 求余数 服务器...")
    mcp.run() 