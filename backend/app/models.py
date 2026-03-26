from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Plesso(Base):
    __tablename__ = "plessi"

    id = Column(Integer, primary_key=True, index=True)
    codice = Column(String, unique=True, index=True)
    nome = Column(String)
    indirizzo = Column(String)

    classi = relationship("Classe", back_populates="plesso")


class Classe(Base):
    __tablename__ = "classi"

    id = Column(Integer, primary_key=True, index=True)
    plesso_id = Column(Integer, ForeignKey("plessi.id"))
    anno = Column(Integer)
    sezione = Column(String)

    plesso = relationship("Plesso", back_populates="classi")


class Docente(Base):
    __tablename__ = "docenti"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cognome = Column(String)
    materia = Column(String)


class Disponibilita(Base):
    __tablename__ = "disponibilita"

    id = Column(Integer, primary_key=True, index=True)
    docente_id = Column(Integer, ForeignKey("docenti.id"))
    giorno = Column(String)
    ora = Column(String)

    docente = relationship("Docente")


class Orario(Base):
    __tablename__ = "orario"

    id = Column(Integer, primary_key=True, index=True)
    classe_id = Column(Integer, ForeignKey("classi.id"))
    docente_id = Column(Integer, ForeignKey("docenti.id"))
    giorno = Column(String)
    ora = Column(String)
    aula = Column(String)

    docente = relationship("Docente")
    classe = relationship("Classe")


class Assenza(Base):
    __tablename__ = "assenze"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    classe_id = Column(Integer, ForeignKey("classi.id"))
    alunno = Column(String)
    motivo = Column(String)

    classe = relationship("Classe")

