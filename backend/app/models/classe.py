from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Classe(Base):
    __tablename__ = "classi"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    plesso_id = Column(Integer, ForeignKey("plessi.id"), nullable=False)

    # RELAZIONE CORRETTA
    plesso = relationship("Plesso", back_populates="classi")
