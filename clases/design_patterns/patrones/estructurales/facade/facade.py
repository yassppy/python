"""
Patrón Facade:

Qué es: Proporciona una interfaz simplificada a una biblioteca,
un framework o cualquier otro grupo complejo de clases.

Cuándo usarlo: Cuando un subsistema es complejo y tiene muchas
clases con dependencias entre sí, y el cliente solo necesita
acceder a una funcionalidad puntual sin conocer los detalles internos.

Para qué: Reducir el acoplamiento entre el código cliente y el
subsistema, ocultando su complejidad detrás de un punto de
entrada único.

Ejemplo:
    Descripción: Crea un sistema de cine en casa que incluya los
    siguientes subsistemas:
    - Proyector: debe tener métodos para encender y apagar.
    - Reproductor Blu-ray: debe tener métodos para reproducir y
      detener la reproducción.
    - Sistema de sonido: debe tener métodos para encender y apagar.
    - Facade: debe tener métodos para encender y apagar todo el
      sistema de cine en casa.
"""


class Proyector:
    """subsistema proyector"""

    def encender(self):
        print("Proyector encendido")

    def apagar(self):
        print("Proyector apagado")


class ReproductorBluRay:
    """subsistema reproductor Blu-ray"""

    def reproducir(self):
        print("Reproductor Blu-ray reproduciendo")

    def detener(self):
        print("Reproductor Blu-ray detenido")


class SistemaSonido:
    """subsistema de sonido"""

    def encender(self):
        print("Sistema de sonido encendido")

    def apagar(self):
        print("Sistema de sonido apagado")


class Facade:
    """Facade: debe tener métodos para encender y apagar todo el
    sistema de cine en casa."""

    def __init__(self):
        self.proyector = Proyector()
        self.reproductor = ReproductorBluRay()
        self.sistema_sonido = SistemaSonido()

    def encender(self):
        print("Encendiendo sistema de cine en casa...")
        self.proyector.encender()
        self.reproductor.reproducir()
        self.sistema_sonido.encender()

    def apagar(self):
        print("Apagando sistema de cine en casa...")
        self.proyector.apagar()
        self.reproductor.detener()
        self.sistema_sonido.apagar()


if __name__ == "__main__":
    facade = Facade()
    facade.encender()
    facade.apagar()
