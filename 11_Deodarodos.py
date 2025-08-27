def Decorador(funcion):
    def funcion_modificada():
        print("antes de la función ")
        funcion()
        print("después de la función ") 
    return funcion_modificada
# def saludar():
#     print("Hola, ¿qué tal?")

# saludo_modificado = Decorador(saludar)
# saludo_modificado()  

@Decorador
def despedir():
    print("Adiós, hasta luego")

despedir()