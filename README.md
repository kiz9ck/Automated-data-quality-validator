# Automated Data Quality Validator

## 📌 Overview
An automated ETL pipeline developed in Python to validate data quality in a simulated enterprise environment. The tool ingests raw CSV data, detects corrupt records based on business logic, and loads clean data into a SQL database for analysis.

## 🚀 Key Features
* **Automated Validation:** Checks for null values, duplicates, and data type mismatches.
* **Business Logic Enforcement:** Validates logic rules (e.g., salaries must be positive, email formats).
* **Error Reporting:** Separates corrupted data into a `processed/error_report.csv` for audit.
* **SQL Integration:** Stores valid records in SQLite for persistent storage.

## 🛠 Tech Stack
* **Python 3.x**
* **Pandas & NumPy** (Data Processing)
* **SQLAlchemy & SQLite** (Database)

## 📂 Project Structure
```text
data_validator/
├── data/               # Storage for raw CSVs and SQLite DB
├── src/
│   ├── generator.py    # Generates dummy data with intentional errors
│   ├── validator.py    # Core validation logic (Class-based)
│   ├── database.py     # SQL handling
│   └── analysis.py     # Post-processing verification
└── main.py             # Entry point for the ETL pipeline