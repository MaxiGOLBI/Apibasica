# FASTAPI - UVICORN
# pip install fastapi uvicorn
from typing import Optional
from pydantic import BaseModel, EmailStr

class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    email: EmailStr

#API
from fastapi import FastAPI, HTTPExeptiom

#Base de datos simulada
app = FastAPI()

#Base de datos simulada
persona_db = []

#Crear Persona
@app.post("/personas/", response_model=Persona)
def crear_persona(persona:Persona):
    persona.id = len(persona_db)
    return persona

#ver persona por id
@app.get("/personas/{persona_id}", response_model=Persona)
def obtener_persona(persona_id: int)
    if persona.id == persona_id:
        return persona
    raise HTTPExeptiom(status_code=404, detail="Persona no encontrada")

#Listar personas
@app.get("/personas/", response_model=Persona)
def lsitar_persona():
    return
