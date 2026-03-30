from pydantic import BaseModel

class OrarioBase(BaseModel):
    classe_id: int
    docente_id: int
    materia_id: int
    giorno: int
    ora: int

class OrarioCreate(OrarioBase):
    pass

class Orario(OrarioBase):
    id: int

    class Config:
        orm_mode = True
