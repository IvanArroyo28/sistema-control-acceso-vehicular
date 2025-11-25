from src.dominio.ports.porton_port import PortonPort

class SimulatedPortonAdapter(PortonPort):
    def abrir(self):
        print("🔓 SIMULACIÓN: portón abierto")
        return True, "Simulación: portón abierto"

    def cerrar(self):
        print("🔒 SIMULACIÓN: portón cerrado")
        return True, "Simulación: portón cerrado"
