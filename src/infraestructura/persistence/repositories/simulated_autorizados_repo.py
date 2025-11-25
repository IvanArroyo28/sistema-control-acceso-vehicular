from typing import Optional
from src.dominio.entities.vehiculo_autorizado import VehiculoAutorizado
from src.dominio.ports.autorizados_port import AutorizadosPort

class SimulatedAutorizadosRepository(AutorizadosPort):

    # Base de datos simulada
    AUTORIZADOS = {"ABC123", "XYZ987", "AAA111"}

    def buscar_por_placa(self, placa: str) -> Optional[VehiculoAutorizado]:
        if placa.upper() in self.AUTORIZADOS:
            return VehiculoAutorizado(placa)
        return None
