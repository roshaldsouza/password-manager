import sqlite3
try:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test (id INT);")
    cursor.execute("INSERT INTO test VALUES (1);")
    print("SQLite working! Version:", sqlite3.sqlite_version)
except Exception as e:
    print("ERROR:", e)