import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG

print("Using DB config:", DB_CONFIG)

def get_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
get_connection()