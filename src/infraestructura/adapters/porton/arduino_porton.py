import os
import serial
from src.dominio.ports.porton_port import PortonPort

class ArduinoPortonAdapter(PortonPort):
    def __init__(self):
        self.modo_simulacion = os.getenv("MODO_SIMULACION", "true").lower() == "true"
        self.puerto = os.getenv("PUERTO_ARDUINO", "COM4")
        self.baudrate = int(os.getenv("BAUDRATE", "9600"))

        if self.modo_simulacion:
            print("🔧 MODO SIMULACIÓN ACTIVADO — Arduino NO requerido")
            self.arduino = None
            return

        try:
            self.arduino = serial.Serial(self.puerto, self.baudrate)
            print(f"🔌 Arduino conectado en {self.puerto}")
        except Exception as e:
            self.arduino = None
            print(f"⚠ Error conectando al Arduino: {e}")

    def abrir(self):
        # --- Simulación ---
        if self.modo_simulacion:
            print("🔓 SIMULACIÓN: portón abierto")
            return True, "Simulación: portón abierto"

        # --- Validación ---
        if not self.arduino:
            return False, f"No se pudo abrir el puerto {self.puerto}. Arduino no conectado."

        # --- Acción real ---
        try:
            self.arduino.write(b'1')
            return True, "Portón abierto correctamente"
        except Exception as e:
            return False, f"Error al enviar señal al Arduino: {e}"

    def cerrar(self):
        if self.modo_simulacion:
            return True, "Simulación: portón cerrado"

        if not self.arduino:
            return False, f"No se pudo cerrar el puerto {self.puerto}. Arduino no conectado."

        try:
            self.arduino.write(b'0')
            return True, "Portón cerrado correctamente"
        except Exception as e:
            return False, f"Error al enviar señal al Arduino: {e}"
