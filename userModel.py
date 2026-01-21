from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum


class Genero(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    otro = "otro"


class Rol(str, Enum):
    admin = "admin"
    user = "user"
    invitado = "invitado"


class Usuario(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Rol]
