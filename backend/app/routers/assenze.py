from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from datetime import date

router = APIRouter(prefix="/api/assenze", tags=["Assenze"])

@router.get("/")
def get_assenze(db: Session = Depends(get_db)):
    return db.query(models.Assenza).all()

@router.post("/")
def create_assenza(assenza: dict, db: Session = Depends(get_db)):
    nuova = models.Assenza(
        data=date.fromisoformat(assenza["data"]),
        classe_id=assenza["classe_id"],
        alunno=assenza["alunno"],
        motivo=assenza["motivo"]
    )
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova

@router.delete("/{assenza_id}")
def delete_assenza(assenza_id: int, db: Session = Depends(get_db)):
    assenza = db.query(models.Assenza).filter(models.Assenza.id == assenza_id).first()
    if not assenza:
        raise HTTPException(404, "Assenza non trovata")
    db.delete(assenza)
    db.commit()
    return {"ok": True}

