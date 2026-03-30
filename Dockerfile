FROM python:3.11-slim

WORKDIR /app

# Copia requirements dalla cartella backend
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia la cartella app dalla cartella backend
COPY backend/app ./app

ENV PORT=8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
