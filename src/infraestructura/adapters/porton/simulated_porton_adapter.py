class SimulatedPortonAdapter:
    def __init__(self):
        self.estado = "cerrado"

    def abrir(self):
        self.estado = "abierto"
        return True, "Simulación: portón abierto"

    def cerrar(self):
        self.estado = "cerrado"
        return True, "Simulación: portón cerrado"

    def obtener_estado(self):
        return f"Simulación: portón {self.estado}"
