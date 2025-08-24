class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola, estoy hablando un poco")

class Empleado:
    def __init__(self, puesto, salario):
        self.puesto = puesto
        self.salario = salario
    def presentarse(self):
        return f"Me llamo {self.nombre} y mi puesto es {self.puesto}" # la función presentarse no tiene sentido aquí pq la clase no tiene nombre ni puesto


class Jefe(Persona, Empleado):  # ⬅️ herencia múltiple
    def __init__(self, nombre, edad, nacionalidad, puesto, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)   # inicializa Persona
        Empleado.__init__(self, puesto, salario)            # inicializa Empleado
        self.empresa = empresa
    def presentarse(self):
        return f"Soy {self.nombre}, jefe en {self.empresa}, y mi puesto es {self.puesto}"

# --- Código principal ---
roberto = Jefe("Roberto", 43, "Argentino", "CEO", 50000, "ASICXXI")


print(roberto.presentarse())

# --- Pruebas de herencia ---
print(issubclass(Jefe, Persona))   # True  (Jefe hereda de Persona)
print(issubclass(Persona, Jefe))   # False (Persona NO hereda de Jefe)

print(isinstance(roberto, Jefe))     # True  (roberto es un Jefe)
print(isinstance(roberto, Persona))  # True  (roberto también es Persona)
print(isinstance(roberto, Empleado)) # True  (y también es Empleado)