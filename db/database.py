# import psycopg2
# from psycopg2 import sql
# from psycopg2.extras import RealDictCursor
# from db.config import DB_CONFIG

# print("Using DB config:", DB_CONFIG)

# def get_connection():
#     """Establish a connection to the PostgreSQL database."""
#     try:
#         conn = psycopg2.connect(**DB_CONFIG)
#         print("Database connection established successfully.")
#         return conn
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")
#         return None
    
# get_connection()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import declarative_base
from db.config import DB_CONFIG
from db.config import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()
def get_db():
    # """Dependency to get a database session.""" -DEPENDANCY INJECTION
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

