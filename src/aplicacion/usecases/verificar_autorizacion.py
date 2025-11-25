class VerificarAutorizacionUseCase:
    def __init__(self, repo_autorizados, adapter_porton):
        self.repo = repo_autorizados
        self.porton = adapter_porton

    def ejecutar(self, placa: str):
        vehiculo = self.repo.buscar_por_placa(placa)

        if vehiculo:
            # Abrir el portón
            self.porton.abrir()
            return {
                "permitido": True,
                "mensaje": f"Acceso concedido a {placa}. Portón abierto."
            }

        return {
            "permitido": False,
            "mensaje": f"Acceso denegado. Vehículo {placa} NO autorizado."
        }
