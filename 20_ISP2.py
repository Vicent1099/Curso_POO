# Principio de segregación de la interfaz
#el cliente no deberia de verse obligado a depender de interfaces que no usa

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Dormilón(ABC):
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
        print("Trabajando") # no hace falta agregar los métodos que no servían

robot = Robot()
robot.trabajar()
humano = Humano()
humano.trabajar()
robot.comer()  # Error: 'Robot' object has no attribute 'comer'
