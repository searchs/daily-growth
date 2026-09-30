# SQLAlchemy ORM quickstart

Consolidated from the historical `in-few-steps` repository.

An ORM maps database tables to Python objects so application code can work with records without embedding SQL everywhere. SQLAlchemy provides both a SQL expression layer and ORM facilities.

## Install

```bash
uv add sqlalchemy
```

Add the database driver required by your target database, for example `psycopg` for PostgreSQL.

## Define a model

```python
from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]


engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(engine)
```

## Insert and query

```python
with Session(engine) as session:
    session.add(User(name="John Doe", age=30))
    session.commit()

with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(user.id, user.name, user.age)
```

## Production notes

- Do not hard-code database passwords in source files.
- Use migrations such as Alembic rather than `create_all()` for evolving production schemas.
- Define transaction boundaries explicitly.
- Keep persistence concerns behind application/domain boundaries where appropriate.
