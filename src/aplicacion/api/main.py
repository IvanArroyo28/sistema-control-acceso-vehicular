from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # ← carga el archivo .env

from src.aplicacion.api.controllers.porton_controller import router as porton_router

app = FastAPI()

app.include_router(porton_router)
