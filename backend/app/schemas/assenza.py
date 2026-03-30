from pydantic import BaseModel

class AssenzaBase(BaseModel):
    docente_id: int
    data: str
    ora: int
    motivo: str | None = None

class AssenzaCreate(AssenzaBase):
    pass

class Assenza(AssenzaBase):
    id: int

    class Config:
        orm_mode = True
