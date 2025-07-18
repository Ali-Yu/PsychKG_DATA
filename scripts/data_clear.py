import sqlite3

# 连接到 SQLite 数据库（如果没有则创建一个名为 'test.db' 的数据库文件）
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 获取所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 删除所有表
for table in tables:
    table_name = table[0]
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print(f"Table {table_name} deleted.")

# 提交更改并关闭连接
conn.commit()
conn.close()