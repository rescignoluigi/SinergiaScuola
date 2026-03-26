from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/api/disponibilita", tags=["Disponibilità"])

@router.get("/")
def get_disponibilita(db: Session = Depends(get_db)):
    return db.query(models.Disponibilita).all()

@router.post("/")
def create_disponibilita(slot: dict, db: Session = Depends(get_db)):
    nuovo = models.Disponibilita(
        docente_id=slot["docente_id"],
        giorno=slot["giorno"],
        ora=slot["ora"]
    )
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.delete("/{slot_id}")
def delete_disponibilita(slot_id: int, db: Session = Depends(get_db)):
    slot = db.query(models.Disponibilita).filter(models.Disponibilita.id == slot_id).first()
    if not slot:
        raise HTTPException(404, "Disponibilità non trovata")
    db.delete(slot)
    db.commit()
    return {"ok": True}

