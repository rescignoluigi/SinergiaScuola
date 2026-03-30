from pydantic import BaseModel

class PlessoBase(BaseModel):
    codice: str
    nome: str
    indirizzo: str | None = None

class PlessoCreate(PlessoBase):
    pass

class Plesso(PlessoBase):
    id: int

    class Config:
        orm_mode = True
