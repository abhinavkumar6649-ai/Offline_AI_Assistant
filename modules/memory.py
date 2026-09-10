import sqlite3
import os

DB_PATH = "data/memory.db"


def create_database():

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Long-term memories
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Conversation history
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
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

    cursor.execute(
        "SELECT value FROM memories WHERE key = ? ORDER BY id DESC LIMIT 1",
        (key,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def save_conversation(role, content):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversation (role, content)
        VALUES (?, ?)
    """, (role, content))

    conn.commit()
    conn.close()


def get_conversation(limit=10):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, content
        FROM conversation
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    rows.reverse()

    return [
        {
            "role": role,
            "content": content
        }
        for role, content in rows
    ]


def clear_conversation():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM conversation")

    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_database()

    save_memory("test_key", "test_value")

    print("Retrieved memory:", get_memory("test_key"))

    save_conversation("user", "Hello Jarvis")
    save_conversation("assistant", "Hello! How can I help you?")

    print("Conversation:")
    print(get_conversation())
