class CerrarPortonUseCase:
    def __init__(self, adapter):
        self.adapter = adapter

    def ejecutar(self):
        success, message = self.adapter.cerrar()
        return {
            "exito": success,
            "mensaje": message
        }
