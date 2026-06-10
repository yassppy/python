"""
Construir un sistema de notificaciones que se pueda enviar a diferentes medios como email, SMS, WhatsApp

Principio de sustitución de liskov:
los objetos de una clase padre deben poder reemplazarse por objetos de una clase hija sin que altere
el comportamiento del programa, si agrego otra clase hija no debe ocurrir ningún problema.
"""


class Notificador:
    def enviar(self, mensaje):
        pass


class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}...")


class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")


class WhatsappNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando Whatsapp: {mensaje}")


## La función debe funcionar con cualquier hijo
def enviar_notificacion(notificador: Notificador, mensaje):
    notificador.enviar(mensaje)


email = EmailNotificador()
enviar_notificacion(email, "Hola")
