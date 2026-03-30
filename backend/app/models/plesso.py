from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Plesso(Base):
    __tablename__ = "plessi"

    id = Column(Integer, primary_key=True, index=True)
    codice = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    indirizzo = Column(String, nullable=False)

    # RELAZIONE CORRETTA
    classi = relationship("Classe", back_populates="plesso")
