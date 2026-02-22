# 🚀 Data Warehouse ETL Pipeline (Industry-Style Project)

## 📌 Project Overview

This project is a **production-style Data Engineering pipeline** that builds and maintains a Data Warehouse using **Python, PostgreSQL, and automated ETL workflows**.

The system simulates how real companies (Amazon, Flipkart, Uber, etc.) continuously ingest transactional data, transform it, and generate analytics-ready datasets.

Instead of static demo data, this project includes a **data generator** that creates new orders automatically — allowing the warehouse to behave like a real growing system.

---

## 🏗️ Architecture

```
Data Generator
      ↓
orders.csv (Source System)
      ↓
Staging Layer (PostgreSQL)
      ↓
Warehouse Layer (Star Schema)
      ↓
Analytics Tables
      ↓
Business Insights
```

---

## ⚙️ Tech Stack

* Python 3
* PostgreSQL
* Pandas
* psycopg2
* Linux / Ubuntu
* Git & GitHub
* GitHub Actions (Automation)

---

## 📂 Project Structure

```
data_warehouse/
│
├── data/
│   └── orders.csv              # Source data
│
├── scripts/
│   ├── init_db.py              # Database & schema initialization
│   ├── init_db.sql             # Warehouse schema
│   ├── load_staging.py         # Incremental data ingestion
│   └── run_transform.py        # Warehouse transformations
│
├── logs/
│   └── pipeline.log            # Pipeline execution logs
│
├── pipeline.py                 # Main ETL Orchestrator
├── generate_orders.py          # Data generator (NEW DATA SIMULATION)
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Workflow

### Step 1 — Database Initialization

Automatically creates:

* staging schema
* warehouse schema
* analytics schema
* fact & dimension tables

---

### Step 2 — Data Generation

`generate_orders.py` simulates new business transactions by adding new records to:

```
data/orders.csv
```

This mimics real production systems where data keeps arriving.

---

### Step 3 — Incremental Loading (ETL)

Pipeline loads **only new records** using:

```
SELECT MAX(order_id)
```

This ensures:

* No duplicate loads
* Idempotent pipeline
* Production-safe ingestion

---

### Step 4 — Transformation

Data moves from:

```
staging → warehouse → analytics
```

Star schema includes:

* `sales_fact`
* `date_dim`
* `customer_dim`
* `product_dim`

---

### Step 5 — Analytics Layer

Example output:

```
analytics.monthly_sales
```

Provides business insights like revenue trends.

---

## ▶️ How To Run

### 1️⃣ Setup Environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2️⃣ Configure Database

Create `.env` file:

```
DB_NAME=sales_warehouse
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 3️⃣ Run Pipeline

```
python pipeline.py
```

Expected output:

```
Database ready ✅
Loading data into staging...
Warehouse Updated Successfully
```

---

## 🤖 Automation

Pipeline can run automatically using:

* GitHub Actions (cloud execution)
* Cron Jobs (Linux scheduler)

This simulates real Data Engineering production workflows.

---

## 📊 Example Insights

Run inside PostgreSQL:

```
SELECT * FROM analytics.monthly_sales;
```

Output:

* Monthly revenue
* Aggregated business metrics
* Analytics-ready datasets

---

## ⭐ Key Data Engineering Concepts Implemented

* ETL Pipeline Design
* Incremental Loading
* Idempotent Processing
* Staging Layer Architecture
* Star Schema Modeling
* Pipeline Orchestration
* Logging & Monitoring
* Automated Deployment

---

## 🎯 Learning Outcome

This project demonstrates how a real Data Engineer:

* Ingests growing datasets
* Builds scalable warehouses
* Automates pipelines
* Produces analytics-ready data

---

## 👨‍💻 Author

**Dhruv Kesarwani**

Aspiring Data Engineer building industry-level data systems.

---

## 🚀 Future Improvements

* Apache Airflow orchestration
* Streaming ingestion (Kafka)
* Cloud deployment (AWS/GCP)
* Dashboard integration (Power BI / Superset)

---

⭐ If you found this useful, consider giving the repository a star!
