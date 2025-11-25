from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# === Carga segura del archivo .env desde la raíz del proyecto ===
CURRENT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.abspath(os.path.join(CURRENT_FILE, "../../../.."))
ENV_PATH = os.path.join(BASE_DIR, ".env")

print("Cargando .env desde:", ENV_PATH)

load_dotenv(ENV_PATH)
# ================================================================

# Importamos los routers de la api
from src.aplicacion.api.controllers.porton_controller import router as porton_router
from src.aplicacion.api.controllers.acceso_controller import router as acceso_router

# Creamos la instancia fast API
app = FastAPI()

# ←–––––– CORS ––––––→
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],   # permite POST, PUT, GET, OPTIONS, etc
    allow_headers=["*"],
)

# Montamos los routers
app.include_router(porton_router)
app.include_router(acceso_router)
