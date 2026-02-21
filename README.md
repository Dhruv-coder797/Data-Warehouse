# 🏗️ Automated End-to-End Data Warehouse Pipeline

## 📌 Overview
This project demonstrates a **production-style Data Engineering pipeline** that builds and maintains a Data Warehouse using Python and PostgreSQL.

The system automatically:
- Initializes database schemas & tables
- Loads raw CSV data into staging
- Transforms data into Star Schema
- Performs incremental loading
- Updates analytics tables
- Runs automatically using Linux Cron

No manual database setup is required.

---

## 🧱 Architecture

---

## ⚙️ Tech Stack

- Python
- PostgreSQL
- Pandas
- psycopg2
- Linux (WSL Ubuntu)
- Git & GitHub
- Cron Scheduler

---

## 📂 Project Structure

---

## 🔄 Pipeline Workflow

1. Auto-create schemas and tables (if missing)
2. Detect last processed record
3. Load only new data (Incremental Load)
4. Populate dimension tables
5. Update fact table
6. Refresh analytics layer
7. Write execution logs

---

## ✅ Key Features

- ✅ Automated database initialization
- ✅ Incremental ETL processing
- ✅ Production-safe path handling
- ✅ Logging system
- ✅ Cron-based automation
- ✅ Clone & Run setup

---

## 🚀 Setup Instructions

### 1️⃣ Clone repository

### 2️⃣ Create virtual environment

### 3️⃣ Install dependencies

### 4️⃣ Configure environment variables

Create `.env` file:

### 5️⃣ Run pipeline

### 5️⃣ Run pipeline

Database and tables will be created automatically.

---

## ⏱️ Automation (Cron)

Example cron job:

Runs pipeline daily at 2 AM.

---

## 📊 Example Output

- Updated warehouse tables
- Monthly revenue analytics
- Execution logs inside `/logs`

---

## 🎯 Learning Outcomes

This project demonstrates:

- Data Warehouse Design
- ETL Pipeline Engineering
- Incremental Data Loading
- Automation & Scheduling
- Deployment across systems
- Production-style project structure

---

## 👨‍💻 Author

Dhruv Kesarwani  
Aspiring Data Engineer 🚀
