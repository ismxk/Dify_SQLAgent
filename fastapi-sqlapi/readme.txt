项目结构：
fastapi-sqlapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── database.py
├── requirements.txt
├── client.py
└── .env

安装依赖：
pip install -r requirements.txt

启动服务端：
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

运行客户端测试：
python client.py
