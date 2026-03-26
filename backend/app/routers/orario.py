from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/api/orario", tags=["Orario"])

@router.get("/")
def get_orario(db: Session = Depends(get_db)):
    return db.query(models.Orario).all()

@router.post("/")
def create_orario(riga: dict, db: Session = Depends(get_db)):
    nuova = models.Orario(
        classe_id=riga["classe_id"],
        docente_id=riga["docente_id"],
        giorno=riga["giorno"],
        ora=riga["ora"],
        aula=riga["aula"]
    )
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova

@router.delete("/{riga_id}")
def delete_orario(riga_id: int, db: Session = Depends(get_db)):
    riga = db.query(models.Orario).filter(models.Orario.id == riga_id).first()
    if not riga:
        raise HTTPException(404, "Riga orario non trovata")
    db.delete(riga)
    db.commit()
    return {"ok": True}

