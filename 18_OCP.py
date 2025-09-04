# se deberia de poder agregar nuevas funcionalidades sin cambiar el codigo funete

class Notificador():
    def notificar(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

        def notificar(self):
            raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando email a {self.usuario}:")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}:")