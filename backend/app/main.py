from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ============================
# MODELLI
# ============================

class Plesso(BaseModel):
    id: int
    nome: str
    indirizzo: str | None = None

class Classe(BaseModel):
    id: int
    nome: str
    sezione: str
    plesso_id: int


# ============================
# DATABASE IN MEMORIA (TEMPORANEO)
# ============================

plessi_db: list[Plesso] = []
classi_db: list[Classe] = []


# ============================
# ENDPOINT DI STATO
# ============================

@app.get("/health")
def health():
    return {"status": "SinergiaScuola backend attivo"}


# ============================
# PLESSI
# ============================

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


# ============================
# CLASSI
# ============================

@app.get("/classi", response_model=List[Classe])
def lista_classi():
    return classi_db

@app.post("/classi", response_model=Classe)
def crea_classe(classe: Classe):
    # Controllo ID duplicato
    for c in classi_db:
        if c.id == classe.id:
            raise HTTPException(status_code=400, detail="ID classe già esistente")

    # Controllo che il plesso esista
    if not any(p.id == classe.plesso_id for p in plessi_db):
        raise HTTPException(status_code=400, detail="Plesso non esistente")

    classi_db.append(classe)
    return classe

@app.get("/classi/{classe_id}", response_model=Classe)
def dettaglio_classe(classe_id: int):
    for c in classi_db:
        if c.id == classe_id:
            return c
    raise HTTPException(status_code=404, detail="Classe non trovata")

@app.delete("/classi/{classe_id}")
def elimina_classe(classe_id: int):
    global classi_db
    classi_db = [c for c in classi_db if c.id != classe_id]
    return {"status": "classe eliminata"}

