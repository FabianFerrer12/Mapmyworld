from fastapi import HTTPException
from app.database import get_connection
from app.models import Category, CategoryCreate

class CategoryService:
    
    @staticmethod
    #Se crea la función para insertar las categorias
    def create_category(category_create: CategoryCreate) -> Category:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories (name, description) VALUES (?, ?)",
                       (category_create.name, category_create.description))
        category_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return Category(id=category_id, **category_create.dict())