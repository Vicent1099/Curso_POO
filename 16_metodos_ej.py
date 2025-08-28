#personajes en un juego que se pueden fusionar con habilidades mejoradas

class Personaje:
    def __init__(self, nombre, fuerza, magia, defensa, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.fuerza = fuerza
        self.magia = magia
        self.defensa = defensa

    def __repr__(self):
        return f"Personaje: {self.nombre}, Nivel: {self.nivel}, Fuerza: {self.fuerza}, Magia: {self.magia}, Defensa: {self.defensa}"
    
    def __add__(self, otro):
        
        nuevo_nombre = self.nombre + "-" + otro.nombre
        nuevo_nivel = self.nivel + otro.nivel
        self_fuerza = self.fuerza + (self.fuerza * 0.1 * otro.nivel)

goku = Personaje("Goku", 90, 70, 80, 5)
vegeta = Personaje("Vegeta", 85, 65, 75, 4)
gogeta = goku + vegeta
print(gogeta)