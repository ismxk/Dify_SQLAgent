# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(c: int, d: int) -> int:
    """subtract two numbers"""
    return c - d

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """divide two numbers"""
    return a / b

# 启动服务器
if __name__ == "__main__":
    print("启动 MCP 数学服务器...")
    mcp.run() 