from fastapi import APIRouter
from pydantic import BaseModel

from src.aplicacion.usecases.verificar_autorizacion import VerificarAutorizacionUseCase
from src.infraestructura.persistence.repositories.simulated_autorizados_repo import SimulatedAutorizadosRepository
from src.aplicacion.api.controllers.porton_controller import get_adapter

router = APIRouter(prefix="/acceso", tags=["Acceso Vehicular"])

class PlacaRequest(BaseModel):
    placa: str


@router.post("/vehiculo")
def verificar_acceso(data: PlacaRequest):
    repo = SimulatedAutorizadosRepository()
    adapter_porton = get_adapter()

    usecase = VerificarAutorizacionUseCase(repo, adapter_porton)
    return usecase.ejecutar(data.placa)
