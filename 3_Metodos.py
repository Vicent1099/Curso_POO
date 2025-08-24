#  un método es una función
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print("Estas llamando")
        print(f"Colgaste la llamada desde tu {self.modelo}")
    def colgar(self):
        print(f"Colgaste la llamada desde tu {self.modelo}")

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 5", "60MP")

celular2.colgar()


