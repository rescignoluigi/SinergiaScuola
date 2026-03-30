from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Docente(Base):
    __tablename__ = "docenti"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # In futuro: relazione con disponibilità e orario
    disponibilita = relationship("Disponibilita", back_populates="docente", cascade="all, delete")
    orario = relationship("Orario", back_populates="docente", cascade="all, delete")
