from fastapi import APIRouter
from src.aplicacion.usecases.abrir_porton import AbrirPortonUseCase
from src.aplicacion.usecases.cerrar_porton import CerrarPortonUseCase

from src.infraestructura.adapters.porton.arduino_porton import ArduinoPortonAdapter
from src.infraestructura.adapters.porton.simulated_porton_adapter import SimulatedPortonAdapter

from src.crosscutting.config import Config

from src.aplicacion.usecases.estado_porton import EstadoPortonUseCase

#para consultar historial
from src.infraestructura.persistence.repositories.porton_eventos_repo import PortonEventosRepo

router = APIRouter(prefix="/porton", tags=["Portón"])


def get_adapter():
    if Config.MODO_SIMULACION:
        return SimulatedPortonAdapter()
    return ArduinoPortonAdapter(
        port=Config.PUERTO_ARDUINO,
        baudrate=Config.BAUDRATE_ARDUINO
    )


@router.post("/abrir")
def abrir_porton():
    adapter = get_adapter()
    use_case = AbrirPortonUseCase(adapter)
    return use_case.ejecutar()

@router.post("/cerrar")
def cerrar_porton():
    adapter = get_adapter()
    use_case = CerrarPortonUseCase(adapter)
    return use_case.ejecutar()

@router.get("/estado")
def obtener_estado_porton():
    adapter = get_adapter()
    use_case = EstadoPortonUseCase(adapter)
    return use_case.ejecutar()

#consultar historial
@router.get("/historial")
def historial_porton():
    repo = PortonEventosRepo()
    return repo.obtener_eventos()



