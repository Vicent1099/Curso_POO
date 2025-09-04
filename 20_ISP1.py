# Principio de segregación de la interfaz
#el cliente no deberia de verse obligado a depender de interfaces que no usa

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("Trabajando")

    def comer(self):
        pass  # Los robots no comen pero lanza error si no se implementa

    def dormir(self):
        pass  # Los robots no comen pero lanza error si no se implementa