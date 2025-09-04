#la clase b puede usar las funciones de la clase a

# class Ave:
#     def volar(self):
#         return 'Estoy volando'

# class Pinguino(Ave):
#     def volar(self):
#         return ("Los pingüinos no pueden volar")

# def hacer_volar(ave = Ave):
#     return ave.volar()
# print(hacer_volar(Pinguino()))  # Los pingüinos no pueden volar

class Ave:
    pass

class Avevoladora(Ave): # funciones de las aves voladoras
    def volar(self):
        return 'Estoy volando'

class Avenovoladora(Ave): # poner las funciones de las aves no voladoras
    def volar(self):
        return ("Los pingüinos no pueden volar")