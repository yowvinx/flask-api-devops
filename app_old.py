from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FOLDER = 'data'
DATA_FILE = os.path.join(DATA_FOLDER, 'data.json')

# Buat folder dan file jika belum ada
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Endpoint GET: Mengambil seluruh data
@app.route('/data', methods=['GET'])
def get_data():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return jsonify(data), 200

# Endpoint POST: Menambahkan data baru jika ID belum ada
@app.route('/data', methods=['POST'])
def post_data():
    new_items = request.get_json()

    # Validasi format data harus berupa list
    if not isinstance(new_items, list):
        return jsonify({"error": "Data harus berupa array of objects"}), 400

    # Baca data lama
    with open(DATA_FILE, 'r') as file:
        existing_data = json.load(file)

    existing_ids = {item["id"] for item in existing_data}
    seen_ids = set()  # Untuk mengecek duplikat dalam array POST

    non_duplicate_items = []
    for item in new_items:
        item_id = item.get("id")
        if item_id is None:
            continue  # Lewatkan item tanpa ID

        if item_id not in existing_ids and item_id not in seen_ids:
            non_duplicate_items.append(item)
            seen_ids.add(item_id)

    # Gabungkan dan simpan data
    updated_data = existing_data + non_duplicate_items
    with open(DATA_FILE, 'w') as file:
        json.dump(updated_data, file, indent=2)

    return jsonify({
        "message": f"{len(non_duplicate_items)} item berhasil ditambahkan",
        "ignored_duplicates": len(new_items) - len(non_duplicate_items)
    }), 201

# Jalankan Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
