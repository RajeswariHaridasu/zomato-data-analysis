# Zomato SQL queries — README

Purpose
- SQL queries to analyze a compact Zomato sample dataset and demonstrate typical business/EDA questions (counts by location, ratings by type, online-order/book-table adoption, top restaurants by votes, cuisines, etc).
- The repository already contains a generic SQL file: `sql/zomato_analysis.sql`.

Files
- sql/zomato_analysis.sql — generic SQL analysis queries (engine-agnostic where possible).
- sql/README.md — this file (how to run and engine-specific tips).

How to run (overview)
- Load your CSV into a SQL table called `zomato_sample` (or update queries to reference your table name).
- Execute `sql/zomato_analysis.sql` using your SQL engine of choice (examples below).
- The generic file assumes columns exist with names similar to the Zomato sample (e.g., `rate`, `votes`, `rest_type`, `online_order`, `book_table`, `cuisines`). Some engines will require small syntax adjustments (see Dialect tips).

Recommended quick options (local)
- DuckDB (recommended for local exploration; no DB server required)
  - Install: `pip install duckdb` or use DuckDB CLI
  - Run directly on CSV (no import needed):
    - duckdb CLI:
      ```
      duckdb
      READ CSV AUTO 'data/zomato_sample.csv' (HEADER=TRUE) AS zomato_sample;
      .read sql/zomato_analysis.sql
      ```
    - Python:
      ```python
      import duckdb
      duckdb.execute("INSTALL httpfs; LOAD httpfs;")
      duckdb.query("CREATE OR REPLACE TABLE zomato_sample AS SELECT * FROM read_csv_auto('data/zomato_sample.csv')")
      duckdb.query(open('sql/zomato_analysis.sql').read()).df()
      ```

- PostgreSQL
  1. Create table schema (or let psql infer/import with tools).
  2. Import CSV:
     ```
     psql -d your_db
     \copy zomato_sample FROM 'data/zomato_sample.csv' WITH (FORMAT csv, HEADER true)
     ```
  3. Run SQL:
     ```
     psql -d your_db -f sql/zomato_analysis.sql
     ```

- SQLite (good for small samples)
  1. Create DB and import:
     ```
     sqlite3 zomato.db
     .mode csv
     .import data/zomato_sample.csv zomato_sample
     .exit
     ```
  2. Run SQL from file:
     ```
     sqlite3 zomato.db < sql/zomato_analysis.sql
     ```
  Note: SQLite lacks some analytic functions; you may need to adapt window/regex usage.

- MySQL
  1. Import:
     ```
     LOAD DATA LOCAL INFILE 'data/zomato_sample.csv' 
     INTO TABLE zomato_sample 
     FIELDS TERMINATED BY ',' 
     ENCLOSED BY '"' 
     LINES TERMINATED BY '\n' 
     IGNORE 1 LINES;
     ```
  2. Run SQL using `mysql -u user -p your_db < sql/zomato_analysis.sql`
  Note: syntax differences (regex, string-split) may require changes.

- Google BigQuery
  - Load data to a table and run the queries in the BigQuery UI or via `bq query --use_legacy_sql=false --format=prettyjson < sql/zomato_analysis.sql`.
  - BigQuery has string-splitting and safe-casting helpers; adapt small items as needed.

Dialect tips and common fixes
- rate values: if `rate` contains strings like `4.1/5` or `NEW`, you must parse them to numeric before AVG. Example approaches:
  - PostgreSQL: `CAST(regexp_replace(rate, '/.*$', '') AS NUMERIC)` (guard non-numeric).
  - DuckDB: `CAST(REGEXP_REPLACE(rate, '/.*$', '') AS DOUBLE)` (or use TRY_CAST).
  - SQLite/MySQL: use substring/replace functions or preprocess in Python/ETL.
- votes: if `votes` contains non-digit characters, remove non-digits first or cast safely.
- approx cost: remove commas before casting (e.g., `regexp_replace(cost, ',', '')`).
- percentage calculation: some engines don't support `SUM(COUNT(*)) OVER ()`. Use a subquery:
