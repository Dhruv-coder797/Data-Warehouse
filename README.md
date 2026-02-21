# 🏗️ End-to-End Data Warehouse Pipeline (PostgreSQL + Python)

## 📌 Project Overview
This project demonstrates an end-to-end Data Engineering pipeline that builds a **Data Warehouse** from raw CSV data using Python and PostgreSQL.

The pipeline automatically:
- Extracts raw data
- Loads into staging tables
- Transforms data into a Star Schema
- Updates analytics tables
- Runs incrementally (loads only new records)

---

## 🧱 Architecture

---

## ⚙️ Tech Stack

- Python 3
- PostgreSQL
- Pandas
- psycopg2
- Linux (WSL Ubuntu)
- Git & GitHub

---

## 📂 Project Structure

---

## 🔄 Pipeline Workflow

1. Read CSV data using Pandas
2. Detect last processed record
3. Load only new records (Incremental Load)
4. Insert data into staging tables
5. Transform data into:
   - Fact Table
   - Dimension Tables
6. Refresh analytics layer

---

## ✅ Features

- Incremental data loading
- Automated pipeline execution
- Logging & error handling
- Environment variable configuration (.env)
- Modular ETL design

---

## 🚀 How to Run

### 1️⃣ Clone repository

### 2️⃣ Create virtual environment

### 3️⃣ Install dependencies

### 4️⃣ Setup environment variables

Create `.env` file:

### 5️⃣ Run pipeline

---

## 📊 Example Output

- Clean warehouse tables
- Monthly sales analytics
- Automated incremental updates

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Data Warehouse Modeling
- ETL Pipeline Design
- Incremental Processing
- PostgreSQL Data Engineering
- Production-style project structure

---

## 👨‍💻 Author

Dhruv Kesarwani  
Aspiring Data Engineer 🚀
