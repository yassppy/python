"""
Patrón Abstract Factory

Qué es: Es un patrón de diseño creacional que permite crear
familias de objetos relacionados (por ejemplo, varios productos
de un mismo estilo) sin especificar sus clases concretas.

Cuándo usarlo: Cuando el código necesita trabajar con varias
familias de productos relacionados, y se debe garantizar que
los productos de una misma familia se usen juntos, sin acoplar
el código cliente a clases concretas.

Para qué: Aislar la creación de objetos relacionados y asegurar
la consistencia entre productos de una misma familia (por
ejemplo, evitar mezclar una silla moderna con un sofá victoriano),
facilitando cambiar toda la familia de productos sin tocar el
código cliente.

Ejemplo del patrón Abstract Factory: familias de muebles
(moderno vs. victoriano).

La fábrica abstracta garantiza que el cliente siempre obtenga
una silla y un sofá del MISMO estilo, sin tener que conocer
las clases concretas ni preocuparse por mezclarlas.
"""

from abc import ABC, abstractmethod


# Productos abstractos
class Silla(ABC):
    @abstractmethod
    def descripcion(self) -> str: ...


class Sofa(ABC):
    @abstractmethod
    def descripcion(self) -> str: ...


# Productos concretos: familia moderna
class SillaModerna(Silla):
    def descripcion(self) -> str:
        return "Silla moderna de líneas rectas y metal"


class SofaModerno(Sofa):
    def descripcion(self) -> str:
        return "Sofá moderno de cuero minimalista"


# Productos concretos: familia victoriana
class SillaVictoriana(Silla):
    def descripcion(self) -> str:
        return "Silla victoriana con tallados en madera"


class SofaVictoriano(Sofa):
    def descripcion(self) -> str:
        return "Sofá victoriano tapizado con terciopelo"


# Fábrica abstracta
class FabricaMuebles(ABC):
    @abstractmethod
    def crear_silla(self) -> Silla: ...

    @abstractmethod
    def crear_sofa(self) -> Sofa: ...


# Fábricas concretas
class FabricaMueblesModernos(FabricaMuebles):
    def crear_silla(self) -> Silla:
        return SillaModerna()

    def crear_sofa(self) -> Sofa:
        return SofaModerno()


class FabricaMueblesVictorianos(FabricaMuebles):
    def crear_silla(self) -> Silla:
        return SillaVictoriana()

    def crear_sofa(self) -> Sofa:
        return SofaVictoriano()


# Cliente: trabaja solo con la interfaz FabricaMuebles,
# nunca con las clases concretas
def amueblar_sala(fabrica: FabricaMuebles) -> None:
    silla = fabrica.crear_silla()
    sofa = fabrica.crear_sofa()
    print(f"- {silla.descripcion()}")
    print(f"- {sofa.descripcion()}")


if __name__ == "__main__":
    print("Amueblando sala con estilo moderno:")
    amueblar_sala(FabricaMueblesModernos())

    print("\nAmueblando sala con estilo victoriano:")
    amueblar_sala(FabricaMueblesVictorianos())
