import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

print("Initializing database...")

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

with open("scripts/init_db.sql", "r") as f:
    cur.execute(f.read())

conn.commit()

cur.close()
conn.close()

print("Database ready ✅")
