import os
from app import create_app
from app.db.database import init_db  # import fungsi init_db

app = create_app()

if __name__ == "__main__":
    init_db()  # inisialisasi database jika belum ada tabelnya
    port = int(os.environ.get("PORT", 8080)) # default ke 8080, overideable
    app.run(host="0.0.0.0", port=port)
