class AbrirPortonUseCase:
    def __init__(self, adapter):
        self.adapter = adapter

    def ejecutar(self):
        success, message = self.adapter.abrir()
        return {
            "exito": success,
            "mensaje": message
        }
