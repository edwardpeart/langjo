# Langjo Backend

## Local setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Alembic helpers

```bash
python -m alembic revision --autogenerate -m "migration"
python -m alembic upgrade head
python -m alembic downgrade -1
```

Or use the project scripts:

```bash
python -m backend.scripts.alembic_cli migrate
python -m backend.scripts.alembic_cli upgrade
python -m backend.scripts.alembic_cli downgrade
```
