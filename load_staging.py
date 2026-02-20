import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="sales_warehouse",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

df = pd.read_csv("data/orders.csv")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO staging.orders_raw
        VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("Loaded into staging")

