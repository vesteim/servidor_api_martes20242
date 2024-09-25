from pydantic import BaseModel,Field
from datetime import date 

#los DTO son clases que establecen
#el modelo de trasnferencia de datos

class UsuarioDTOPeticion(BaseModel):
    nombres : str
    fechaNacimiento : date
    ubicacion : str
    metaAhorro : float
    class Config:   # trae la informacion de la BD
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id : int
    nombres : str
    metaAhorro : float
    class Config:   
        orm_mode=True


# gastoDTOPeticion
class gastoDTOPeticion(BaseModel):
    idGasto : int
    monto : int
    fecha : str
    descripcion : str
    nombre : str
class gastoDTORespuesta(BaseModel):
    idGasto : int
    monto : int
    fecha : str
    descripcion : str
    nombre : str


# CategoriaDTOPeticion
class CategoriaDTOPeticion:
    idCategoria : int
    nombreCategoria : str
    descripcion : str
    fotoicono : str
    

class CategoriaDTORespuesta:
    idCategoria : int
    nombreCategoria : str
    descripcion : str
    fotoicono : str

# IngresoDTOPeticion

class IngresoDTOPeticion:
    idIngresos: int
    nombreMetodo: str
    descripcion: str

class IngresoDTORespuesta:
    idIngresos: int
    nombreMetodo: str
    descripcion: str

# FacturaDTOPeticion
