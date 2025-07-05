from flask import Flask
from app.routes.data_routes import data_bp
from app.db.database import init_db  # <-- Tambahkan ini

def create_app():
    app = Flask(__name__)
    init_db()  # <-- Pastikan ini dipanggil
    app.register_blueprint(data_bp)
    return app

