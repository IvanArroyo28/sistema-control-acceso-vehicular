from abc import ABC, abstractmethod
from typing import Optional
from src.dominio.entities.vehiculo_autorizado import VehiculoAutorizado

class AutorizadosPort(ABC):

    @abstractmethod
    def buscar_por_placa(self, placa: str) -> Optional[VehiculoAutorizado]:
        pass
