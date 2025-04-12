# Dify_SQLAgent
The project aims to use the latest AI technology platform to build a dedicated Agent, achieve semi-automated business processes, and comprehensively improve production efficiency and reduce production costs.

## 项目介绍

**Dify_SQLAgent** 项目旨在利用最新的人工智能技术平台，构建一个专属的 Agent，以实现半自动化的业务流程，全面提升生产效率并降低生产成本。项目的核心目标是基于大模型领域的 Dify 和 MCP 技术，构建金融大数据数据库的智能 Agent。

该项目通过构建一套 SQL 查询服务接口与 Dify 工作流，实现了自然语言转 SQL 的能力，使得非专业技术人员也能够轻松操作和查询业务数据。

## 项目结构

### FastAPI 部分

该部分实现了 SQL 查询服务接口，支持通过 FastAPI 提供 RESTful API 接口与数据库进行交互。

项目结构：

fastapi-sqlapi/ ├── app/ │ ├── init.py │ ├── main.py │ ├── database.py │ └── .env ├── requirements.txt └── client.py

### MCP 部分

该部分实现了 MCP（Model Control Protocol）服务器，以 Cursor 作为客户端，接入 Dify 智能体 API，使用户能够通过简单的接口操作业务数据表。

项目结构：

dify-mcp/ ├── dify_agent_server.py ├── test_agent_dify.py ├── mcp.json └── requirements.txt

## 安装与部署

### FastAPI 部分

#### 安装依赖

1. 进入 FastAPI 项目目录，并安装依赖：

   ```bash
   pip install -r requirements.txt

2. 启动 FastAPI 服务端：

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   
3. 运行客户端测试，验证接口是否正常工作：

   ```bash
   python client.py

### MCP Server 部分

#### 安装依赖

1. 进入 MCP 项目目录，并安装依赖：

   ```bash
   pip install -r requirements.txt

2. 启动 MCP 服务器，提供 Dify API 访问功能：

   ```bash
   mcp run D:\LLM学习\MCP\dify_agent_server.py
   
3. 测试 Dify API 是否正常工作：

   ```bash
   python test_agent_dify.py

## 配置说明
### FastAPI 部分
在 .env 文件中，您可以设置数据库连接和其他环境变量。

### MCP 部分
在 dify_agent_server.py 文件中，您可以配置以下内容：

1. DIFY_API_KEY: Dify API 密钥

2. DIFY_API_URL: Dify API URL

### 注意事项
1. 确保您的 Dify API 密钥有效。

2. 确保您的网络环境可以访问 Dify API。

3. 在生产环境中，确保配置了正确的数据库连接字符串，并且已经正确部署数据库。

## 功能说明
### FastAPI 功能
1. SQL 查询服务接口
使用 FastAPI 构建业务数据库查询服务，支持通过 SQL 语句进行数据的增、删、改、查操作。

2. 自然语言转 SQL 查询
使用 Dify 工作流，将用户输入的自然语言查询转换为 SQL 语句并执行，返回查询结果。

### MCP 功能
1. MCP 服务
使用 MCP 服务与 Dify API 进行通信，通过简化的接口使用户能够轻松操作业务数据表。

2. Dify API 测试
通过 test_agent_dify.py 测试脚本，可以验证与 Dify API 的连接是否正常。
