from flask import Blueprint, request, jsonify
from app.services.data_services import load_data, find_by_id, add_item
from app.utils.helpers import validate_data

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_all_data():
    data = load_data()
    return jsonify(data), 200

@data_bp.route('/data/<int:item_id>', methods=['GET'])
def get_data_by_id(item_id):
    item = find_by_id(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({'error': 'Data tidak ditemukan'}), 404

@data_bp.route('/data', methods=['POST'])
def create_data():
    new_data = request.get_json()
    is_valid, message = validate_data(new_data)
    if not is_valid:
        return jsonify({'error': message}), 400
    success, result = add_item(new_data)
    if success:
        return jsonify(result), 201
    return jsonify({'error': result}), 400
