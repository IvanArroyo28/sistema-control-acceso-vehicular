from src.infraestructura.persistence.repositories.porton_eventos_repo import PortonEventosRepo

class AbrirPortonUseCase:
    def __init__(self, adapter):
        self.adapter = adapter
        self.repo = PortonEventosRepo()

    def ejecutar(self):
        exito, mensaje = self.adapter.abrir()
        self.repo.agregar_evento("ABRIR", mensaje)

        return {
            "exito": exito,
            "mensaje": mensaje
        }

#class AbrirPortonUseCase:
#    def __init__(self, adapter):
#        self.adapter = adapter
#
#    def ejecutar(self):
#        success, message = self.adapter.abrir()
#        return {
#           "exito": success,
#            "mensaje": message
#        }