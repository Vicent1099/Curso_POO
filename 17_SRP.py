class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion


class Tanquedecombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = Tanquedecombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())   # 0
auto.mover(10)
print(auto.obtener_posicion())   # 10
auto.mover(20)
print(auto.obtener_posicion())   # 30
print(tanque.obtener_combustible())  # 100 - (10/2 + 20/2) = 85
auto.mover(50)
print(auto.obtener_posicion())   # 80
print(tanque.obtener_combustible())  # 60
auto.mover(100)                  
print(auto.obtener_posicion())   
