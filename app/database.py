import sqlite3

DB_FILE = "mapmyworld.db"
#Se llama la conexion
def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn
#Se crean las tablas
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY,
            location_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            recommended_item TEXT NOT NULL,
            freshness_score INTEGER NOT NULL,
            FOREIGN KEY (location_id) REFERENCES locations(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)
    conn.commit()
    conn.close()
