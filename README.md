# World Population ETL Pipeline

ETL pipeline that extracts world population CSV data,
transforms and cleans it using Pandas, and loads
it into PostgreSQL for analysis.

## Tech Stack
- Python 3
- Pandas
- PostgreSQL
- SQLAlchemy

## Pipeline Steps
1. Extract — Load raw CSV data (234 countries)
2. Transform — Clean, rename, categorize population data
3. Load — Store in PostgreSQL for analysis

## SQL Analysis
Used window functions to rank countries by population

## How to Run
pip install pandas psycopg2-binary sqlalchemy
python etl_pipeline.py
