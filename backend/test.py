import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=ai-crack-db.database.windows.net;"
    "DATABASE=ai-crack-db;"
    "UID=soteria8;"
    "PWD=adminadmin1!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ 연결 성공!")
except Exception as e:
    print("❌ 연결 실패:", e)

