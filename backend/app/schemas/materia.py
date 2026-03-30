from pydantic import BaseModel

class MateriaBase(BaseModel):
    nome: str

class MateriaCreate(MateriaBase):
    pass

class Materia(MateriaBase):
    id: int

    class Config:
        orm_mode = True
