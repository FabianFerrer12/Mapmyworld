from pydantic import BaseModel

#Creacion de modelos para las tablas de la base de datos
class LocationBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class RecommendationBase(BaseModel):
    location_id: int
    category_id: int
    recommended_item: str
    freshness_score: int

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int

    class Config:
        orm_mode = True
