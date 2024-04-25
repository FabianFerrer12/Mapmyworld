# Mapmyworld
Prueba tecnica ORBIDI


Para ejecutar el proyecto primero se ejecuta la instalacion de las dependecias 
pip install fastapi uvicorn pydantic
Y luego el comando  uvicorn app.main:app --reload para que arranque el aplicativo
Generando este una base de datos SQLITE llamada mapmyworld

Luego se ejecuta python seeds.py para generar unas semillas aleatorias para que se creen en la base de datos

Apartir de ahi se puede probar el api con sus diferentes rutas

1. Creacion de locaciones

Se puede probar mediante Postman o ThunderClient o su aplicativo de peticiones favorito enviando de la siguiente forma la estructura por ejemplo

Poniendo como ruta http://localhost:8000/locations

Y pasandole en el cuerpo la siguiente estructura
{
    "name": "Mi Ubicación Favorita",
    "latitude": 40.7128,
    "longitude": -74.0060
}
El cual retornara los datos creados y el id con el cual fue creado

2. Creacion de categorias 

Se puede probar mediante Postman o ThunderClient o su aplicativo de peticiones favorito enviando de la siguiente forma la estructura por ejemplo

Poniendo como ruta http://localhost:8000/categories

Y pasandole en el cuerpo la siguiente estructura
{
    "name": "Restaurante",
    "description": "Lugares para disfrutar de comida deliciosa"
}
El cual retornara los datos creados y el id con el cual fue creado
3.Recomendador de exploracion 

Se puede probar mediante Postman o ThunderClient o su aplicativo de peticiones favorito enviando de la siguiente forma la estructura por ejemplo

Poniendo como ruta http://localhost:8000/recommendations

El cual devolvera 10 sugerencias de combinaciones de Ubicación - categoria que no han sido revisadas en lo ultimos 30 dias, priorizando las que nunca se han revisado
