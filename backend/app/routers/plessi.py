from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/api/plessi", tags=["Plessi"])

@router.get("/")
def get_plessi(db: Session = Depends(get_db)):
    return db.query(models.Plesso).all()

@router.post("/")
def create_plesso(plesso: dict, db: Session = Depends(get_db)):
    nuovo = models.Plesso(
        codice=plesso["codice"],
        nome=plesso["nome"],
        indirizzo=plesso["indirizzo"]
    )
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.delete("/{plesso_id}")
def delete_plesso(plesso_id: int, db: Session = Depends(get_db)):
    plesso = db.query(models.Plesso).filter(models.Plesso.id == plesso_id).first()
    if not plesso:
        raise HTTPException(404, "Plesso non trovato")
    db.delete(plesso)
    db.commit()
    return {"ok": True}

