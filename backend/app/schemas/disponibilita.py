from pydantic import BaseModel

class DisponibilitaBase(BaseModel):
    docente_id: int
    giorno: str
    ora: int

class DisponibilitaCreate(DisponibilitaBase):
    pass

class Disponibilita(DisponibilitaBase):
    id: int

    class Config:
        orm_mode = True
