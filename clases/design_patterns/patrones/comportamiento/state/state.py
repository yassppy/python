"""
Patrón State

Qué es: Es un patrón de diseño de comportamiento que permite a
un objeto alterar su comportamiento cuando su estado interno
cambia. Parece como si el objeto cambiara de clase.

Cuándo usarlo: Cuando el comportamiento de un objeto depende de
su estado y cambia en tiempo de ejecución, especialmente si el
código tiene muchos condicionales (if/else o switch) que
verifican el estado actual del objeto.

Para qué: Eliminar esos condicionales encapsulando cada estado
en su propia clase, de modo que agregar un nuevo estado no
requiera modificar el código existente, solo añadir una clase más.

Ejemplo del patrón State: sistema de control de una lavadora.

Estados:
Apagada -> EsperandoInstrucciones -> Lavando -> Enjuagando -> Centrifugando -> EsperandoInstrucciones

Cada estado responde distinto a las mismas acciones
(encender, seleccionar_programa, lavar, enjuagar, centrifugar).
"""

from abc import ABC, abstractmethod


class EstadoLavadora(ABC):
    @abstractmethod
    def encender(self, lavadora):
        pass

    @abstractmethod
    def seleccionar_programa(self, lavadora):
        pass

    @abstractmethod
    def lavar(self, lavadora):
        pass

    @abstractmethod
    def enjuagar(self, lavadora):
        pass

    @abstractmethod
    def centrifugar(self, lavadora):
        pass

    @abstractmethod
    def nombre(self) -> str:
        pass


# Estados concretos
class Apagada(EstadoLavadora):
    def encender(self, lavadora):
        print("Lavadora encendida")
        lavadora.cambiar_estado(EsperandoInstrucciones())

    def seleccionar_programa(self, lavadora):
        print("No se puede seleccionar programa: la lavadora está apagada")

    def lavar(self, lavadora):
        print("No se puede lavar: la lavadora está apagada")

    def enjuagar(self, lavadora):
        print("No se puede enjuagar: la lavadora está apagada")

    def centrifugar(self, lavadora):
        print("No se puede centrifugar: la lavadora está apagada")

    def nombre(self):
        return "Apagada"


class EsperandoInstrucciones(EstadoLavadora):
    def encender(self, lavadora):
        print("La lavadora ya está encendida")

    def seleccionar_programa(self, lavadora):
        print("Programa seleccionado, iniciando lavado")
        lavadora.cambiar_estado(Lavando())

    def lavar(self, lavadora):
        print("Debes seleccionar un programa antes de lavar")

    def enjuagar(self, lavadora):
        print("Debes seleccionar un programa antes de enjuagar")

    def centrifugar(self, lavadora):
        print("Debes seleccionar un programa antes de centrifugar")

    def nombre(self):
        return "Esperando instrucciones"


class Lavando(EstadoLavadora):
    def encender(self, lavadora):
        print("La lavadora ya está en marcha")

    def seleccionar_programa(self, lavadora):
        print("Ya hay un programa en curso")

    def lavar(self, lavadora):
        print("Lavado terminado, pasando a enjuague")
        lavadora.cambiar_estado(Enjuagando())

    def enjuagar(self, lavadora):
        print("Aún no termina el lavado")

    def centrifugar(self, lavadora):
        print("Aún no termina el lavado")

    def nombre(self):
        return "Lavando"


class Enjuagando(EstadoLavadora):
    def encender(self, lavadora):
        print("La lavadora ya está en marcha")

    def seleccionar_programa(self, lavadora):
        print("Ya hay un programa en curso")

    def lavar(self, lavadora):
        print("El lavado ya terminó")

    def enjuagar(self, lavadora):
        print("Enjuague terminado, pasando a centrifugado")
        lavadora.cambiar_estado(Centrifugando())

    def centrifugar(self, lavadora):
        print("Aún no termina el enjuague")

    def nombre(self):
        return "Enjuagando"


class Centrifugando(EstadoLavadora):
    def encender(self, lavadora):
        print("La lavadora ya está en marcha")

    def seleccionar_programa(self, lavadora):
        print("Ya hay un programa en curso")

    def lavar(self, lavadora):
        print("El lavado ya terminó")

    def enjuagar(self, lavadora):
        print("El enjuague ya terminó")

    def centrifugar(self, lavadora):
        print("Centrifugado terminado, ciclo completo")
        lavadora.cambiar_estado(EsperandoInstrucciones())

    def nombre(self):
        return "Centrifugando"


# Context
class Lavadora:
    def __init__(self):
        self.estado = Apagada()

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def encender(self):
        self.estado.encender(self)

    def seleccionar_programa(self):
        self.estado.seleccionar_programa(self)

    def lavar(self):
        self.estado.lavar(self)

    def enjuagar(self):
        self.estado.enjuagar(self)

    def centrifugar(self):
        self.estado.centrifugar(self)

    def estado_actual(self):
        return self.estado.nombre()


# Cliente
if __name__ == "__main__":
    lavadora = Lavadora()

    print("--- Intento usarla sin encenderla ---")
    lavadora.lavar()

    print("\n--- Ciclo normal completo ---")
    print(f"Estado: {lavadora.estado_actual()}")
    lavadora.encender()

    print(f"Estado: {lavadora.estado_actual()}")
    lavadora.seleccionar_programa()

    print(f"Estado: {lavadora.estado_actual()}")
    lavadora.lavar()

    print(f"Estado: {lavadora.estado_actual()}")
    lavadora.enjuagar()

    print(f"Estado: {lavadora.estado_actual()}")
    lavadora.centrifugar()

    print(f"Estado final: {lavadora.estado_actual()}")
