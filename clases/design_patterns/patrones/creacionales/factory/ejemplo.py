"""
El patrón FACTORY: una fábrica que crea objetos por ti, para que tu código no dependa de
saber exactamente qué clase instanciar ni cómo hacerlo. Esto es útil para
manejar objetos que pueden cambiar su tipo o que requieren una lógica de inicialización
específica

Imaginemos que estamos desarrollando un sistema de notificaciones, y podemos tener
diferentes tipos de notificaciones (Email, SMS, Push). Usaremos el Patrón Factory para
crear estos objetos.
"""

from abc import ABC, abstractmethod


## Interfaz de notificaciones
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


## clases concretas con sus propias implementaciones
class Email(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando email: {mensaje}")


class SMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando SMS: {mensaje}")


class Push(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando push: {mensaje}")


## Fábrica de notificaciones
class NotificacionFactory:
    def crear_notificacion(self, tipo: str) -> Notificacion:
        """Crear el objeto dependiendo del tipo de notificación solicitado"""
        if tipo == "email":
            return Email()
        elif tipo == "sms":
            return SMS()
        elif tipo == "push":
            return Push()
        else:
            raise ValueError("Tipo de notificación no válido")


if __name__ == "__main__":
    tipo_notificacion = input("Ingrese el tipo de notificación (email, sms, push): ")
    factory = NotificacionFactory()
    notificacion = factory.crear_notificacion(tipo_notificacion)
    notificacion.enviar("Hola, esto es una notificación")
