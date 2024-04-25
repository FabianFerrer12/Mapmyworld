import sqlite3
from datetime import datetime, timedelta
import random
import string

# Conexión a la base de datos SQLite
conn = sqlite3.connect("mapmyworld.db")
cursor = conn.cursor()

locations_data = []
for i in range(1, 31):
    name = f"Location {i}"
    latitude = round(random.uniform(-90, 90), 6)  
    longitude = round(random.uniform(-180, 180), 6)  
    locations_data.append((name, latitude, longitude))

cursor.executemany("INSERT INTO locations (name, latitude, longitude) VALUES (?, ?, ?)", locations_data)

categories_data = []
for i in range(1, 31):
    name = f"Category {i}"
    description = " ".join(random.choices(string.ascii_letters + string.digits, k=20))  
    categories_data.append((name, description))


cursor.executemany("INSERT INTO categories (name, description) VALUES (?, ?)", categories_data)


recommendations_data = []
for loc_id in range(1, 31):  
    for cat_id in range(1, 31): 
        recommended_item = f"Recommended Item for Location {loc_id} and Category {cat_id}"
        freshness_score = random.randint(1, 100)  
        recommendations_data.append((loc_id, cat_id, recommended_item, freshness_score))


cursor.executemany("INSERT INTO recommendations (location_id, category_id, recommended_item, freshness_score) VALUES (?, ?, ?, ?)", recommendations_data)


conn.commit()
conn.close()

print("Seeds generados correctamente.")
