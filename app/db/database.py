# app/db/database.py
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../../data/app.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Agar hasil query bisa diakses seperti dict
    return conn

def init_db():
  try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
  except sqlite3.Error as e:
      print(f"Database error: {e}")
  finally:
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
