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