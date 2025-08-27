# es un clase que no se puede instanciar pero que se puede usar como plantilla
from abc import ABC, abstractmethod #abc es una clase auxiliar

#abstractmethod es un decorador que avisa que es un método abstracto
#un metodo abstarcto es un método que no tiene implementación en la clase base
#las clases que heredan de la clase abstracta deben implementar los métodos abstractos

class Persona(ABC):  # hereda de ABC
    @abstractmethod
    def __init__(self, nombre, edad, sexo, trabajo):
        self.nombre = nombre
        self.edad = edad   
        self.sexo = sexo
        self.trabajo = trabajo
    
    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años, soy {self.sexo} y trabajo como {self.trabajo}"
    
#persona1 = Persona("Ana", 30, "Mujer", "Ingeniera") # Error: no se puede instanciar una clase abstracta

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, trabajo, carrera):
        super().__init__(nombre, edad, sexo, trabajo)
        self.carrera = carrera
    def trabajar(self):
        return f"{self.nombre} está estudiando {self.carrera}"
    
persona2 = Estudiante("Luis", 22, "Hombre", "Estudiante", "Informática")
print(persona2.presentarse())