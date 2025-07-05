# Gunakan image Python sebagai base
FROM python:3.10-slim

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Salin semua file dari direktori lokal ke dalam container
COPY . .

# Install dependencies dari requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Jalankan aplikasi
CMD ["python", "run.py"]
