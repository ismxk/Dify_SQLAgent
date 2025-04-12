# 数据库连接模块

import os
import pyodbc
from dotenv import load_dotenv

# 将.env放在根目录，load_dotenv()改为：
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


class SQLServer:
    def __init__(self):
        self.conn_str = (
            f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )

    def get_connection(self):
        try:
            return pyodbc.connect(self.conn_str)
        except pyodbc.Error as e:
            raise RuntimeError(f"数据库连接失败: {str(e)}")


db = SQLServer()