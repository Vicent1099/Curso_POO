# permite la clase hija acceder a los métodos y propedaades de la padre y cambiar sus propiedades.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self. nombre = nombre
        self. edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,empleo, salario):
        super().__init__(nombre, edad, nacionalidad) # hereda los atributos de la clase padre (Persona) los métodos se heredan
        self.empleo = empleo
        self.salario = salario

roberto = Empleado("Roberto", 43, "Argentino", "")

print(roberto.edad)
roberto.hablar()