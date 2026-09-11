from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


import app.models  # noqa: F401  - registra todos los modelos en Base.metadata