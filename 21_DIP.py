#no se debe de depender de interfacez añadidas
# las implementaciones de alto nivel no deben de depender de las de bajo nivel

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         pass

# class CorrectirOrtografico:
#     def __init(self): #el corrector está vinculado al diccionario, si queremos cambiar la forma de revisar las palabras hay que cambiar esta clase 
#         self.diccionario = Diccionario()
    
#     def correfir_texto(self, texto):
#         pass

from abc import ABC, abstractmethod

class Verificador(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(Verificador):
    def verificar_palabra(self,palabra):
        pass

class CorrectirOrtografico: # esta clase depende de la abstracción de verificador
    def __init__(self, verificador):
        self.verificador = verificador
    
    def vorregir_texto(self, texto):
        pass