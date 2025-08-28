# metodos especiales

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):  # metodo especial para representar el objeto como cadena
        return f"Persona: {self.nombre}, Edad: {self.edad}"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"
# si llamo al objeto, muestro lo que me devuelve el método str
    def __add__(self, otro): #suma objetos
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)

persona = Persona("Ana", 30)
print(persona)  # llama a persona.__str__()

repre = repr(persona)  # llama a persona.__repr__()
resultado = eval(repre)  # evalúa la cadena y crea un nuevo objeto
print(resultado)  # muestra el nuevo objeto creado

pedor = Persona("Pedor", 25)
maria = Persona("Maria", 28)
carlos = Persona("Carlos", 40)

nueva_persona = pedor + maria * carlos
print(nueva_persona)  # Persona: PedorMaria, Edad: 53

