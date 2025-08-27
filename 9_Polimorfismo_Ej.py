
class pago:
    def __init__(self, medio_de_pago, monto):
        self.medio_de_pago = medio_de_pago
        self.monto = monto
    def pagar(self):
        return f"Has pagado con {self.medio_de_pago} un total de {self.monto} euros."



pagos = [("tarjeta", 100), ("efectivo", 50), ("bizum", 75)]
for i in pagos:
    i = pago(i[0], i[1])
    print(i.pagar())