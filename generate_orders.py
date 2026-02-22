import csv
import random
from datetime import datetime, timedelta

file_path = "data/orders.csv"

# ---- CONFIG ----
NUM_NEW_ROWS = 5000   # jitna data chahiye change kar sakte ho
START_ORDER_ID = 9    # last order_id ke baad ka number

# ----------------

start_date = datetime(2024, 1, 1)

rows = []

for i in range(NUM_NEW_ROWS):
    order_id = START_ORDER_ID + i

    random_days = random.randint(0, 120)
    order_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

    customer_id = random.randint(1, 20)
    product_id = random.randint(1, 5)
    quantity = random.randint(1, 5)

    price = random.choice([500, 1000, 1500, 50000])
    total_amount = price * quantity

    rows.append([
        order_id,
        order_date,
        customer_id,
        product_id,
        quantity,
        total_amount
    ])

# append data
with open(file_path, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"{NUM_NEW_ROWS} new orders added ✅")
