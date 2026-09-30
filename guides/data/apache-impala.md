# Apache Impala quickstart

Consolidated from the historical `in-few-steps` repository and corrected to distinguish immutable/file-backed tables from mutable Kudu-backed tables.

## Connect

```bash
impala-shell
```

## File-backed table over CSV data

Upload a file to HDFS:

```bash
hdfs dfs -mkdir -p /data/employees
hdfs dfs -put employees.csv /data/employees/
```

Create an external table:

```sql
CREATE EXTERNAL TABLE employees_csv (
    id INT,
    name STRING,
    age INT,
    salary DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/data/employees';
```

Then query it normally:

```sql
SELECT * FROM employees_csv;
```

For file/HDFS-backed tables, treat the data as append/read-oriented. Row-level `UPDATE` and `DELETE` are not generally available in the same way as a transactional database.

## Mutable data with Kudu

When row-level mutation is required, use an Impala table backed by Kudu (where available/configured). Kudu-backed tables support operations such as `INSERT`, `UPDATE`, `UPSERT` and `DELETE` subject to the table schema and cluster configuration.

## Practical notes

- Prefer Parquet over CSV for analytical workloads once data is normalised.
- Keep raw ingestion and curated analytical datasets separate.
- Refresh/invalidate metadata when external files or schemas change outside Impala.
- Validate the exact Impala/Kudu capabilities against the version deployed in your environment.
