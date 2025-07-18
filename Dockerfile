# Gunakan base image Python resmi
FROM python:3.10-slim

# Set direktori kerja
WORKDIR /app

# Copy file requirements dan install dependensi
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file ke dalam container
COPY . .

# Expose port 8080 agar sesuai dengan gunicorn dan Cloud Run
EXPOSE 8080

# Gunakan gunicorn untuk menjalankan app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "run:app"]
