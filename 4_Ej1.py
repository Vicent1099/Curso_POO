# clase Estudiantes con atributos Nombre edad y Grado, metodos estudiar y devuelva elestudiante con nombre está estaudiandoP
class Estudiante:
    def __init__(self, nombre, edad, grado, estudiando = bool):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.estudiando = estudiando
    
    def estudiar(self):
        if self.estudiando == True:
            print(f"{self.nombre} está estudiando")
        else:
            print(f"{self.nombre} no está estudiando")

nombre = input("Indique su nombre: ")
edad = int(input("Indique la edad: "))
grado = input("Indique el grado: ")
pregunta = input("Estudia mucho el estudiante? Si o no: ")
estudiando = True if pregunta == "si" else False

estudiante1 = Estudiante(nombre, edad, grado, estudiando)

print(f"NOMBRE: {estudiante1.nombre}\nEDAD: {estudiante1.edad}\nGRADO: {estudiante1.grado} ")
estudiante1.estudiar()






