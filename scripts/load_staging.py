import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()
print("Loading data into staging...")
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()



# ✅ Get last processed order_id from warehouse
cur.execute("SELECT COALESCE(MAX(order_id),0) FROM warehouse.sales_fact;")
last_id = cur.fetchone()[0]

print(f"Last processed order_id: {last_id}")

# Read CSV
df = pd.read_csv("data/orders.csv")

# ✅ Keep only NEW records
df = df[df["order_id"] > last_id]

if df.empty:
    print("No new data found.")
else:
    # Clean staging first
    cur.execute("TRUNCATE staging.orders_raw;")

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO staging.orders_raw
            VALUES (%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    print("New records loaded into staging.")

cur.close()
conn.close()
