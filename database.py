import sqlite3

def init_db():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_password(service: str, username: str, encrypted_password: str):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
        (service, username, encrypted_password)
    )
    conn.commit()
    conn.close()