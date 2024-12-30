from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import psycopg
from psycopg.rows import dict_row
from .config import settings
# Properly encoded connection URL
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'



# SQLAlchemy engine and session configuration
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for SQLAlchemy models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# while True:

#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='oluwadarasimi123#', row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#     except Exception as error:
#         print("Connecting to database failed:", error)
#         raise SystemExit(error)
#     break
    
