from fastapi import FastAPI
from dotenv import load_dotenv

from app.Auth.Login.Infraestructure import Login

load_dotenv()


app = FastAPI()
app.include_router(Login.router)