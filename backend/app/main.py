from fastapi import FastAPI
from app.routers import sheets

app = FastAPI()

# Solo il router Google Sheets
app.include_router(sheets.router)

@app.get("/")
def root():
    return {"status": "SinergiaScuola backend attivo (modalità Sheets)"}
