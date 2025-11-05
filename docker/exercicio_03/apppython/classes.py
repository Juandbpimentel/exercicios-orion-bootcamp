from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ComidaBase(BaseModel):
    nome: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)

class ComidaCreate(ComidaBase):
    pass

class Comida(ComidaBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True