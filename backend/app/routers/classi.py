from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/api/classi", tags=["Classi"])

@router.get("/")
def get_classi(db: Session = Depends(get_db)):
    return db.query(models.Classe).all()

@router.post("/")
def create_classe(classe: dict, db: Session = Depends(get_db)):
    nuova = models.Classe(
        plesso_id=classe["plesso_id"],
        anno=classe["anno"],
        sezione=classe["sezione"]
    )
    db.add(nuova)
    db.commit()
    db.refresh(nuova)
    return nuova

@router.delete("/{classe_id}")
def delete_classe(classe_id: int, db: Session = Depends(get_db)):
    classe = db.query(models.Classe).filter(models.Classe.id == classe_id).first()
    if not classe:
        raise HTTPException(404, "Classe non trovata")
    db.delete(classe)
    db.commit()
    return {"ok": True}

