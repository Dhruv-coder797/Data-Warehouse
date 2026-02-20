import psycopg2

print("Starting warehouse transformation...")

conn = psycopg2.connect(
    dbname="sales_warehouse",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# SQL file read karo
with open("scripts/transform.sql", "r") as file:
    sql = file.read()

# Execute SQL transformations
cur.execute(sql)

conn.commit()

cur.close()
conn.close()

print("Warehouse Updated Successfully")
