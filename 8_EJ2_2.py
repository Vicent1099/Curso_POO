class Animal:
    def comer(self):
        return f"El animal come"

class Mamifero:
    def amamantar(self):
        return f"El mamífero amamanta"

class Ave:
    def volar(self):
        return f"El ave vuela"

class Murcielago(Animal, Mamifero, Ave):  # herencia múltiple
    def presentarse(self):
        return f"Soy un murciélago"

print(Murcielago.mro())

murcielago = Murcielago()
print(murcielago.volar())
print(murcielago.amamantar())