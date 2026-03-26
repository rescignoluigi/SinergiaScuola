from fastapi import FastAPI
from .database import Base, engine
from .routers import plessi, classi, materie, docenti, disponibilita, orario, assenze

# Crea le tabelle nel database all'avvio
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registra tutti i router
app.include_router(plessi.router)
app.include_router(classi.router)
app.include_router(materie.router)
app.include_router(docenti.router)
app.include_router(disponibilita.router)
app.include_router(orario.router)
app.include_router(assenze.router)

@app.get("/")
def root():
    return {"status": "SinergiaScuola backend attivo"}




