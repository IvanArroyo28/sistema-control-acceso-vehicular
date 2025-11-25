from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class Config:
    MODO_SIMULACION = os.getenv("MODO_SIMULACION", "true").lower() == "true"
    PUERTO_ARDUINO = os.getenv("PUERTO_ARDUINO", "COM4")
    BAUDRATE_ARDUINO = int(os.getenv("BAUDRATE", 9600))
