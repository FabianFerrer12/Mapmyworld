from fastapi import FastAPI
from app.database import create_tables

app = FastAPI()

# Crea las tablas en la base de datos al iniciar la aplicación
create_tables()

# Importa las rutas y servicios
import app.main