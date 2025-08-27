#manejar la complejidad sin mostrar la interfaz compleja

class Coche:
    def __init__(self):
        self.__estado = 'apagado'

    def encender(self):
        self.__estado = 'encendido'
        return "El coche está encendido."
    
    def conducir(self):
        if self.__estado == 'encendido':
            return "El coche está en marcha."
        else:
            return "No puedes conducir un coche apagado."

mi_coche = Coche()
print(mi_coche.conducir())
mi_coche.encender()
print(mi_coche.conducir())