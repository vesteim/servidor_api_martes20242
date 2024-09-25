from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends 
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.tablassql import Usuario
from app.database.configuration import sessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    try:
        baseDatos=sessionLocal()  #crear el camino de conexion con la bd
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()  # parar todas las peticiones
        raise error #cuenta que paso (el error)

    finally:
        baseDatos.close()  #cerrar peticion    