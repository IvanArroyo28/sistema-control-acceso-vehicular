import json
import os
from datetime import datetime

RUTA_ARCHIVO = "porton_eventos.json"

class PortonEventosRepo:

    def __init__(self):
        # Si el archivo no existe, lo crea vacío
        if not os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, "w") as f:
                json.dump([], f)

    def agregar_evento(self, accion, mensaje):
        evento = {
            "accion": accion,
            "mensaje": mensaje,
            "fecha": datetime.now().isoformat()
        }

        eventos = self.obtener_eventos()
        eventos.append(evento)

        with open(RUTA_ARCHIVO, "w") as f:
            json.dump(eventos, f, indent=4)

    def obtener_eventos(self):
        with open(RUTA_ARCHIVO, "r") as f:
            return json.load(f)
