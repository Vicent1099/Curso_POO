# dar un método a un objeto entendiendo que las propiedades son diferentes
#caminar --> perro, gato, humano andan pero de diferente manera

class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())  

gato = Gato()
perro = Perro()

hacer_sonido(gato)  # Miau
hacer_sonido(perro) # Guau

# también se puede hacer a la incersa

print(gato.sonido())
print(perro.sonido())

# Polimorfismo de herencia

def recorrer(lista):
    for item in lista:
        print(f"El elemento es: {item}")

lista1=[1, 2, 3, 4, 5]
lista2=["Hola", "que", "tal"]
lista3 = "Soy una cadena"

recorrer(lista1)
recorrer(lista2)
recorrer(lista3)  # recorre cada letra