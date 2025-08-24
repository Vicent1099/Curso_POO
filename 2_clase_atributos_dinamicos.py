# Los atributos (self.marca, self.modelo, self.camara) son los que guardan valores dentro del objeto
# cuando llamas Celular("Samsung", "S23", "48MP"), el método __init__ asigna esos valores a los atributos del objeto a través de self.
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung", "S23", "48MP")
print(celular1.marca)



