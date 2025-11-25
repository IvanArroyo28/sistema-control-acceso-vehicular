from fastapi import APIRouter
from src.aplicacion.usecases.abrir_porton import AbrirPortonUseCase
from src.aplicacion.usecases.cerrar_porton import CerrarPortonUseCase

from src.infraestructura.adapters.porton.arduino_porton import ArduinoPortonAdapter
from src.infraestructura.adapters.porton.simulated_porton_adapter import SimulatedPortonAdapter

from src.crosscutting.config import Config

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
