from fastapi import FastAPI
from typing import List
from userModel import Genero, Rol, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        nombre="Carlos",
        apellidos="Cabrera Fosado",
        genero=Genero.masculino,
        roles=[Rol.admin],
    ),
    Usuario(
        nombre="Daniela",
        apellidos="Leon Jimenez",
        genero=Genero.femenino,
        roles=[Rol.user],
    ),
    Usuario(
        nombre="Tania",
        apellidos="Marquez Cabrera",
        genero=Genero.femenino,
        roles=[Rol.admin],
    ),
    Usuario(
        nombre="Abril",
        apellidos="Guzman Pazos",
        genero=Genero.femenino,
        roles=[Rol.invitado],
    ),
]

@app.get("/")
async def root():
    return {"Saludo": "Hola 8b IDGS hijos del tio randi"}

@app.get("/api/v1/users")
async def get_user():
    return db
