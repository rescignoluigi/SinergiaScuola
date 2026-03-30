from pydantic import BaseModel, ConfigDict

class DocenteBase(BaseModel):
    nome: str
    cognome: str
    email: str

class DocenteCreate(DocenteBase):
    pass

class Docente(DocenteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

