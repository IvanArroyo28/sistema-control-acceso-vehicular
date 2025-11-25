#class CerrarPortonUseCase:
#    def __init__(self, adapter):
#        self.adapter = adapter
#
#    def ejecutar(self):
#        success, message = self.adapter.cerrar()
#        return {
#            "exito": success,
#            "mensaje": message
#        }


from src.infraestructura.persistence.repositories.porton_eventos_repo import PortonEventosRepo

class CerrarPortonUseCase:
    def __init__(self, adapter):
        self.adapter = adapter
        self.repo = PortonEventosRepo()

    def ejecutar(self):
        exito, mensaje = self.adapter.cerrar()
        self.repo.agregar_evento("CERRAR", mensaje)

        return {
            "exito": exito,
            "mensaje": mensaje,
            "modo": "SIMULACION"  # se reemplaza luego por Config
        }
