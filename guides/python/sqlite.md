# SQLite with Python

Consolidated from the historical `in-few-steps` repository. The original search example used string interpolation to build SQL; this version uses parameterised queries.

## Connect and create a table

```python
import sqlite3

with sqlite3.connect("users.db") as connection:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date TEXT,
            valid INTEGER NOT NULL DEFAULT 1
        )
        """
    )
```

## Insert safely

```python
with sqlite3.connect("users.db") as connection:
    connection.execute(
        "INSERT INTO users (first_name, last_name, birth_date, valid) VALUES (?, ?, ?, ?)",
        ("John", "Doe", "1990-01-01", 1),
    )
```

## Dynamic search with parameters

```python
def search_user(*, first_name=None, last_name=None, birth_date=None):
    clauses: list[str] = []
    values: list[str] = []

    if first_name:
        clauses.append("first_name = ?")
        values.append(first_name)
    if last_name:
        clauses.append("last_name = ?")
        values.append(last_name)
    if birth_date:
        clauses.append("birth_date = ?")
        values.append(birth_date)

    sql = "SELECT id, first_name, last_name, birth_date, valid FROM users"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)

    with sqlite3.connect("users.db") as connection:
        return connection.execute(sql, values).fetchall()
```

Parameterized queries keep user-supplied values separate from SQL syntax and avoid the injection risk of constructing queries with f-strings.
