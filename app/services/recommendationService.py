from typing import List
from fastapi import HTTPException
from app.database import get_connection
from app.models import  Recommendation, RecommendationCreate

class RecommendationService:
    @staticmethod
    #Se crea la función para obtener las locaciones que sugiere 10 combinaciones de ubicación-categoría que no han sido revisadas en los últimos 30 días,
    def get_recommendations() -> List[Recommendation]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM recommendations
            ORDER BY freshness_score DESC
            LIMIT 10
        """)
        recommendations = [Recommendation(**row) for row in cursor.fetchall()]
        conn.close()
        return recommendations