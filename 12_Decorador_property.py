#el decorador property avisa de que es un getter o setter
class Mi_clase:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado

    @property  # getter
    def nombre(self):
        return self.__nombre

    @nombre.setter  # setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property  # getter
    def edad(self):
        return self.__edad

    @edad.setter  # setter
    def edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")

#se puede usar el punto en vez de llamar a la función
#además actúa como encapsulamiento
#si se quiere cambiar el nombre o la edad, se usa el setter

persona = Mi_clase("Ana", 30)
print(persona.nombre)  # usa el getter

persona.edad = 35     # usa el setter
print(persona.edad)   # usa el getter





