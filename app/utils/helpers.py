import json
from pathlib import Path

DATA_FILE = Path('data/data.json')

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def validate_data(data):
    if not data or 'id' not in data or 'name' not in data:
        return False, 'Data tidak valid. Harus memiliki "id" dan "name".'
    return True, ''
