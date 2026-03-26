from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# ============================
# MODELLI
# ============================

class Plesso(BaseModel):
    id: int
    nome: str
    indirizzo: Optional[str] = None

class Classe(BaseModel):
    id: int
    nome: str
    sezione: str
    plesso_id: int

class Materia(BaseModel):
    id: int
    nome: str

class Docente(BaseModel):
    id: int
    nome: str
    cognome: str
    materie: List[int]  # lista ID materie

class Disponibilita(BaseModel):
    id: int
    docente_id: int
    giorno: str
    ora: int

class Lezione(BaseModel):
    id: int
    classe_id: int
    docente_id: int
    materia_id: int
    giorno: str
    ora: int

class Assenza(BaseModel):
    id: int
    docente_id: int
    giorno: str
    ora: int
    motivo: Optional[str] = None


# ============================
# DATABASE IN MEMORIA
# ============================

plessi_db: List[Plesso] = []
classi_db: List[Classe] = []
materie_db: List[Materia] = []
docenti_db: List[Docente] = []
disponibilita_db: List[Disponibilita] = []
orario_db: List[Lezione] = []
assenze_db: List[Assenza] = []


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
    if any(p.id == plesso.id for p in plessi_db):
        raise HTTPException(status_code=400, detail="ID plesso già esistente")
    plessi_db.append(plesso)
    return plesso

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
    if any(c.id == classe.id for c in classi_db):
        raise HTTPException(status_code=400, detail="ID classe già esistente")
    if not any(p.id == classe.plesso_id for p in plessi_db):
        raise HTTPException(status_code=400, detail="Plesso non esistente")
    classi_db.append(classe)
    return classe

@app.delete("/classi/{classe_id}")
def elimina_classe(classe_id: int):
    global classi_db
    classi_db = [c for c in classi_db if c.id != classe_id]
    return {"status": "classe eliminata"}


# ============================
# MATERIE
# ============================

@app.get("/materie", response_model=List[Materia])
def lista_materie():
    return materie_db

@app.post("/materie", response_model=Materia)
def crea_materia(materia: Materia):
    if any(m.id == materia.id for m in materie_db):
        raise HTTPException(status_code=400, detail="ID materia già esistente")
    materie_db.append(materia)
    return materia

@app.delete("/materie/{materia_id}")
def elimina_materia(materia_id: int):
    global materie_db
    materie_db = [m for m in materie_db if m.id != materia_id]
    return {"status": "materia eliminata"}


# ============================
# DOCENTI
# ============================

@app.get("/docenti", response_model=List[Docente])
def lista_docenti():
    return docenti_db

@app.post("/docenti", response_model=Docente)
def crea_docente(docente: Docente):
    if any(d.id == docente.id for d in docenti_db):
        raise HTTPException(status_code=400, detail="ID docente già esistente")
    for materia_id in docente.materie:
        if not any(m.id == materia_id for m in materie_db):
            raise HTTPException(status_code=400, detail=f"Materia {materia_id} inesistente")
    docenti_db.append(docente)
    return docente

@app.delete("/docenti/{docente_id}")
def elimina_docente(docente_id: int):
    global docenti_db
    docenti_db = [d for d in docenti_db if d.id != docente_id]
    return {"status": "docente eliminato"}


# ============================
# DISPONIBILITÀ DOCENTI
# ============================

@app.get("/disponibilita", response_model=List[Disponibilita])
def lista_disponibilita():
    return disponibilita_db

@app.post("/disponibilita", response_model=Disponibilita)
def crea_disponibilita(disp: Disponibilita):
    if not any(d.id == disp.docente_id for d in docenti_db):
        raise HTTPException(status_code=400, detail="Docente inesistente")
    disponibilita_db.append(disp)
    return disp


# ============================
# ORARIO (LEZIONI)
# ============================

@app.get("/orario", response_model=List[Lezione])
def lista_orario():
    return orario_db

@app.post("/orario", response_model=Lezione)
def crea_lezione(lezione: Lezione):
    if not any(c.id == lezione.classe_id for c in classi_db):
        raise HTTPException(status_code=400, detail="Classe inesistente")
    if not any(d.id == lezione.docente_id for d in docenti_db):
        raise HTTPException(status_code=400, detail="Docente inesistente")
    if not any(m.id == lezione.materia_id for m in materie_db):
        raise HTTPException(status_code=400, detail="Materia inesistente")
    orario_db.append(lezione)
    return lezione


# ============================
# ASSENZE
# ============================

@app.get("/assenze", response_model=List[Assenza])
def lista_assenze():
    return assenze_db

@app.post("/assenze", response_model=Assenza)
def registra_assenza(assenza: Assenza):
    if not any(d.id == assenza.docente_id for d in docenti_db):
        raise HTTPException(status_code=400, detail="Docente inesistente")
    assenze_db.append(assenza)
    return assenza



