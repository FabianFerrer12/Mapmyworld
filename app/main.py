from typing import List
from fastapi import FastAPI
from app.models import Location, LocationCreate, Category, CategoryCreate, Recommendation
from app.services.locationService import LocationService
from app.services.categoryService import CategoryService
from app.services.recommendationService import RecommendationService

app = FastAPI()

#Se genera la ruta para insertar las locaciones
@app.post("/locations/", response_model=Location)
def create_location(location_create: LocationCreate):
    return LocationService.create_location(location_create)
#Se genera la ruta para insertar las categorias
@app.post("/categories/", response_model=Category)
def create_category(category_create: CategoryCreate):
    return CategoryService.create_category(category_create)
#Se genera la ruta para obtener las locaciones que sugiere 10 combinaciones de ubicación-categoría que no han sido revisadas en los últimos 30 días,
@app.get("/recommendations/", response_model=List[Recommendation])
def get_recommendations():
    return RecommendationService.get_recommendations()