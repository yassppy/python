"""
Patrón Observer

Qué es: Es un patrón de diseño de comportamiento que permite
definir un mecanismo de suscripción para notificar a varios
objetos sobre cualquier evento que le suceda al objeto que
están observando.

Cuándo usarlo: Cuando un cambio en el estado de un objeto debe
notificarse a otros objetos, sin que el emisor necesite saber
cuántos son ni quiénes son.

Para qué: Reducir el acoplamiento entre el sujeto (quien cambia
de estado) y los observadores (quienes reaccionan a ese cambio),
permitiendo agregar o quitar observadores en tiempo de ejecución
sin modificar el sujeto.

Ejemplo del patrón Observer: sistema de monitoreo de temperatura
en una fábrica.
"""

from abc import ABC, abstractmethod


# Interfaz Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, temperatura: float) -> None:
        pass


# Observadores concretos
class Registro(Observador):
    def actualizar(self, temperatura: float) -> None:
        print(f"[Registro] Temperatura registrada: {temperatura}°C")


class SistemaAlarma(Observador):
    def actualizar(self, temperatura: float) -> None:
        print(
            f"[Alarma] ¡Temperatura crítica! {temperatura}°C - activando alarma sonora"
        )


class SistemaVentilacion(Observador):
    def actualizar(self, temperatura: float) -> None:
        print(f"[Ventilación] Activando ventiladores para enfriar a {temperatura}°C")


# Sujeto (Subject)
class SensorTemperatura:
    def __init__(self, limite: float):
        self.limite = limite
        self.observadores: list[Observador] = []

    def agregar_observador(self, observador: Observador) -> None:
        self.observadores.append(observador)

    def quitar_observador(self, observador: Observador) -> None:
        self.observadores.remove(observador)

    def notificar(self, temperatura: float) -> None:
        for observador in self.observadores:
            observador.actualizar(temperatura)

    def medir_temperatura(self, temperatura: float) -> None:
        print(f"\nMedición: {temperatura}°C")
        if temperatura > self.limite:
            self.notificar(temperatura)
        else:
            print("Temperatura dentro de los límites normales")


# Cliente
if __name__ == "__main__":
    sensor = SensorTemperatura(limite=80)

    sensor.agregar_observador(Registro())
    sensor.agregar_observador(SistemaAlarma())
    sensor.agregar_observador(SistemaVentilacion())

    lecturas = [65, 72, 85, 90, 78]

    for lectura in lecturas:
        sensor.medir_temperatura(lectura)
