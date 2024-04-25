from fastapi import HTTPException
from app.database import get_connection
from app.models import Location, LocationCreate

class LocationService:
    @staticmethod
    #Se crea la función para insertar las locaciones
    def create_location(location_create: LocationCreate) -> Location:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO locations (name, latitude, longitude) VALUES (?, ?, ?)",
                       (location_create.name, location_create.latitude, location_create.longitude))
        location_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Location(id=location_id, **location_create.dict())