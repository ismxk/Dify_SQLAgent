from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
# from database import db
from app.database import db
import pyodbc
import json
from typing import Dict, Any

app = FastAPI(title="SQL Query API")

# CORS配置（按需调整）。使用 CORSMiddleware 中间件，允许跨源请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/query")
async def execute_query(payload: Dict[str, Any]):
    """
    执行SQL查询

    请求体示例：
    {
        "sql": "SELECT TOP 5 * FROM YourTable",
        "parameters": {}  # 可选参数
    }
    """
    try:
        # 安全警告：实际生产环境应禁用直接执行任意SQL
        if not payload.get("sql"):
            raise HTTPException(status_code=400, detail="缺少SQL语句")

        conn = db.get_connection()
        cursor = conn.cursor()

        # 使用参数化查询防止SQL注入
        sql = payload["sql"]
        params = payload.get("parameters", {})

        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        # 处理结果集
        if cursor.description is None:
            return {"message": "执行成功", "affected_rows": cursor.rowcount}

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return {
            "data": results,
            "row_count": len(results)
        }

    except pyodbc.Error as e:
        raise HTTPException(
            status_code=400,
            detail=f"数据库错误: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"服务器错误: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)