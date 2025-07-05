# app/services/data_services.py

from app.db.database import get_connection

def load_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def find_by_id(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def add_item(new_item):
    name = new_item.get('name')
    description = new_item.get('description', '')

    if not name:
        return False, 'Field "name" wajib diisi.'

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO data (name, description) VALUES (?, ?)", (name, description))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return True, {'id': new_id, 'name': name, 'description': description}
    except Exception as e:
        conn.rollback()
        conn.close()
        return False, str(e)
