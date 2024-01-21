from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated, Generator, Any
from fastapi import Depends
import psycopg2  # Unused import - required for pigar


from os import getenv

SQLALCHEMY_DATABASE_URL = f"sqlite:///database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function is required to provide an unique, auto-closed connection per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Database = Annotated[Session, Depends(get_db)]
