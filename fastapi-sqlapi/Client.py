import aiohttp # aiohttp 是一个用于异步 HTTP 请求的 Python 库，它支持异步操作，适用于需要高并发的场景。
import asyncio
import json


async def query_api(sql: str, params: dict = None):
    url = "http://localhost:8000/api/query"
    payload = {
        "sql": sql,
        "parameters": params or {}
    }

    async with aiohttp.ClientSession() as session:
        # json=payload 让 aiohttp 自动将字典转换为 JSON 格式，并设置 Content-Type: application/json 头。
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                error = await response.text()
                return {"error": f"请求失败 ({response.status})", "detail": error}


# 使用示例
async def main():
    # 示例查询（替换为实际表名）
    sql = """
    SELECT TOP 3 * 
    FROM RReportTask..CT_DACCMg 
    where state=0
    """

    # response = await query_api(sql, params=('2023-01-01',))
    response = await query_api(sql)
    print(json.dumps(response, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())