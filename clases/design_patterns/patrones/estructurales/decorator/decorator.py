"""
Patrón Decorator

Qué es: Es un patrón de diseño estructural que permite añadir
funcionalidades nuevas a un objeto colocándolo dentro de objetos
envolventes especiales que contienen esas funcionalidades.

Cuándo usarlo: Cuando necesitas añadir responsabilidades a
objetos individuales de forma dinámica, sin afectar a otros
objetos de la misma clase, o cuando usar herencia generaría
una explosión de subclases para cubrir cada combinación posible.

Para qué: Evitar crear una subclase distinta para cada combinación
de extras (por ejemplo CafeConLeche, CafeConChocolate,
CafeConLecheYChocolate...), permitiendo combinar comportamientos
envolviendo objetos en capas en tiempo de ejecución.

Ejemplo del patrón Decorator: sistema de pedidos de café.

Permite añadir extras (leche, chocolate) a un café base
envolviendo objetos en capas, sin crear una subclase distinta
para cada combinación posible (CafeConLeche, CafeConChocolate,
CafeConLecheYChocolate, ...).
"""

from abc import ABC, abstractmethod


# Componente abstracto
class Cafe(ABC):
    @abstractmethod
    def costo(self) -> float: ...

    @abstractmethod
    def descripcion(self) -> str: ...


# Componente concreto
class CafeSimple(Cafe):
    def costo(self) -> float:
        return 5

    def descripcion(self) -> str:
        return "Café simple"


# Decorador base: también es un Cafe, y envuelve a otro Cafe
class DecoradorCafe(Cafe):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    def costo(self) -> float:
        return self._cafe.costo()

    def descripcion(self) -> str:
        return self._cafe.descripcion()


# Decoradores concretos
class ConLeche(DecoradorCafe):
    def costo(self) -> float:
        return self._cafe.costo() + 2

    def descripcion(self) -> str:
        return self._cafe.descripcion() + ", con leche"


class ConChocolate(DecoradorCafe):
    def costo(self) -> float:
        return self._cafe.costo() + 3

    def descripcion(self) -> str:
        return self._cafe.descripcion() + ", con chocolate"


# Cliente: cada capa envuelve a la anterior
if __name__ == "__main__":
    cafe = CafeSimple()
    print(f"{cafe.descripcion()} cuesta {cafe.costo()}€")

    cafe_con_leche = ConLeche(cafe)
    print(f"{cafe_con_leche.descripcion()} cuesta {cafe_con_leche.costo()}€")

    cafe_con_leche_y_chocolate = ConChocolate(cafe_con_leche)
    print(
        f"{cafe_con_leche_y_chocolate.descripcion()} cuesta "
        f"{cafe_con_leche_y_chocolate.costo()}€"
    )
