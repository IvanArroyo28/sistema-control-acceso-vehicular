from abc import ABC, abstractmethod

class PortonPort(ABC):

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def cerrar(self):
        pass
