from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ====== MODELLI ======

class Plesso(BaseModel):
    id: int
    nome: str
    indirizzo: str | None = None

# ====== DATABASE IN MEMORIA (PER ORA) ======

plessi_db: list[Plesso] = []

# ====== ENDPOINT DI STATO ======

@app.get("/health")
def health():
    return {"status": "SinergiaScuola backend attivo"}

# ====== PLESSI ======

@app.get("/plessi", response_model=List[Plesso])
def lista_plessi():
    return plessi_db

@app.post("/plessi", response_model=Plesso)
def crea_plesso(plesso: Plesso):
    for p in plessi_db:
        if p.id == plesso.id:
            raise HTTPException(status_code=400, detail="ID plesso già esistente")
    plessi_db.append(plesso)
    return plesso

@app.get("/plessi/{plesso_id}", response_model=Plesso)
def dettaglio_plesso(plesso_id: int):
    for p in plessi_db:
        if p.id == plesso_id:
            return p
    raise HTTPException(status_code=404, detail="Plesso non trovato")

@app.delete("/plessi/{plesso_id}")
def elimina_plesso(plesso_id: int):
    global plessi_db
    plessi_db = [p for p in plessi_db if p.id != plesso_id]
    return {"status": "plesso eliminato"}
