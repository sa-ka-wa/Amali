import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

DB_CONFIG = {
    "host": os.environ.get("PGHOST", "localhost"),
    "port": os.environ.get("PGPORT", 5432),
    "dbname": os.environ.get("PGDATABASE", "calorie_tracker"),
    "user": os.environ.get("PGUSER", "amali_user"),
    "password": os.environ.get("PGPASSWORD", "Amali")
}
print("Using DB config:", DB_CONFIG)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://amali_user:Amali@localhost:5432/calorie_tracker")
if DATABASE_URL:
    DB_CONFIG = {
        "dsn": DATABASE_URL
    }
    print("Using DATABASE_URL for DB config:", DB_CONFIG)