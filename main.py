from fastapi import FastAPI
from dotenv import load_dotenv

from app.Auth.Login.Infraestructure import Login

from config.db.db import engine, SessionLocal
from config.db import models

models.Base.metadata.create_all(bind=engine)

load_dotenv()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.include_router(Login.router)