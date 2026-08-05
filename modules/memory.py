import sqlite3
import os

DB_PATH = "data/memory.db"

def create_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_memory(key, value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memories (key, value)
        VALUES (?, ?)
    """, (key, value))
    conn.commit()
    conn.close()

def get_memory(key):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM memories WHERE key = ?", (key,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0] 
    else:
        return None

if __name__ == "__main__":
    create_database()
    save_memory("test_key", "test_value")
    print("Retrieved memory:", get_memory("test_key"))
