
from pydantic import BaseModel, ValidationError,validator
from typing import List

class Burger(BaseModel):
    prix: float
    description: str
    list_allergene: List[str]
    cuisson: str
    unite: int

    @validator('prix')
    def prix_must_be_positive(cls, v):
        if v < 10 or v > 20:
            raise ValueError('prix doit etre entre 10 et 20')
        return v
    
    @validator('list_allergene')
    def check_list_allergene(cls, v):
        if "crustacé" in v or "poisson" in v or "soja" in v or "céleri" in v or "molusque" in v:
            raise ValueError('Liste des allergenes ne doit pas contenir ces trucs')
        return v
    
    @validator('cuisson')
    def check_cuisson(cls, v):
        if v != "saignant" and v != "a point" and v != "cuit":
            raise ValueError('Cuisson doit etre soit saignant, a point ou bien cuit')
        return v
    
    @validator('unite')
    def check_unite(cls, v):
        if v % 1000 != 0 or v > 65000 or v < 5000:
            raise ValueError('Unite doit etre un multiple de 1000 et entre 5000 et 65000')
        return v
