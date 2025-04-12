import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=10.17.207.185;"
    "DATABASE=RreportTask;"
    "UID=dbinput;"
    "PWD=123456;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT @@version")
    print("连接成功！服务器版本：", cursor.fetchone()[0])
except pyodbc.Error as e:
    print("连接失败：", str(e))