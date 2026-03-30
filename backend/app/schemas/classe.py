from pydantic import BaseModel

class ClasseBase(BaseModel):
    nome: str
    plesso_id: int

class ClasseCreate(ClasseBase):
    pass

class Classe(ClasseBase):
    id: int

    class Config:
        orm_mode = True
