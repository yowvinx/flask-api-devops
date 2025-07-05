from app import create_app
from app.db.database import init_db  # import fungsi init_db

app = create_app()

if __name__ == "__main__":
    init_db()  # inisialisasi database jika belum ada tabelnya
    app.run(debug=True, host="0.0.0.0")
