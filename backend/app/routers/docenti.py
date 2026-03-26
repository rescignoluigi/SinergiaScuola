from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/api/docenti", tags=["Docenti"])

@router.get("/")
def get_docenti(db: Session = Depends(get_db)):
    return db.query(models.Docente).all()

@router.post("/")
def create_docente(docente: dict, db: Session = Depends(get_db)):
    nuovo = models.Docente(
        nome=docente["nome"],
        cognome=docente["cognome"],
        materia=docente["materia"]
    )
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.delete("/{docente_id}")
def delete_docente(docente_id: int, db: Session = Depends(get_db)):
    docente = db.query(models.Docente).filter(models.Docente.id == docente_id).first()
    if not docente:
        raise HTTPException(404, "Docente non trovato")
    db.delete(docente)
    db.commit()
    return {"ok": True}

