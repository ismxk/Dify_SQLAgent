# Dify MCP 集成

这个项目提供了使用MCP（Model Control Protocol）接入Dify智能体API的功能。

## 文件说明

- `dify_server.py`: MCP服务器实现，提供Dify API访问功能
- `test_dify.py`: 测试脚本，用于测试Dify API的访问
- `mcp.json`: MCP配置文件
- `requirements.txt`: 项目依赖列表

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 启动MCP服务器

```bash
mcp run D:\LLM学习\MCP\dify_server.py
```

### 测试Dify API

```bash
python test_dify.py
```

## 配置说明

在`dify_server.py`中，您可以修改以下配置：

- `DIFY_API_KEY`: Dify API密钥
- `DIFY_API_URL`: Dify API URL

## 注意事项

- 请确保您的API密钥有效
- 请确保您的网络环境可以访问Dify API 