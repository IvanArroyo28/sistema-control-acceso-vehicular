from src.crosscutting.config import Config

class EstadoPortonUseCase:
    def __init__(self, adapter):
        self.adapter = adapter

    def ejecutar(self):
        estado = self.adapter.obtener_estado()

        return {
            "exito": True,
            "mensaje": estado,
            "modo": "SIMULACION" if Config.MODO_SIMULACION else "REAL"
        }
