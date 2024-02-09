from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

USER = os.getenv("DB_USER") 
PASSWORD = os.getenv("DB_PASSWORD")
SERVER = os.getenv("DB_SERVER")
DB = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{USER}:{PASSWORD}@{SERVER}/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()