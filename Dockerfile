# Usa Python ufficiale
FROM python:3.11-slim

# Imposta la working directory
WORKDIR /app

# Copia SOLO il backend
COPY backend/ /app/

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Porta esposta
ENV PORT=8080

# Comando di avvio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
