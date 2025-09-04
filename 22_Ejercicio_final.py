from textblob import TextBlob

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] <= polaridad <= rango[1]:  # <= en ambos lados
                return sentimiento
        return Sentimiento("muy negativo", "31") # rojo por defecto

class Sentimiento:
    def __init__(self, nombre, color):  
        self.nombre = nombre   
        self.color = color
    
    def __str__(self):
        return f"\x1b[1;{self.color}m{self.nombre}\x1b[0;37m"


rangos = [
    ((-1.0, -0.3), Sentimiento("negativo", "31")),      # rojo
    ((-0.3, 0.1), Sentimiento("neutral", "34")),       # azul
    ((0.1, 0.6), Sentimiento("positivo", "32")),       # verde
    ((0.6, 1.0), Sentimiento("muy positivo", "92"))    # verde brillante
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    texto = input("Ingrese un texto para analizar sus sentimientos (o 'salir' para terminar): ")
    if texto.lower() == 'salir':
        break
    polaridad = TextBlob(texto).sentiment.polarity
    resultado = analizador.analizar_sentimiento(polaridad)
    print(f"Polaridad: {polaridad:.2f} → Sentimiento: {resultado}")
