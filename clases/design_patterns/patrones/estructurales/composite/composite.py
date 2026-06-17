"""
Patrón Composite

Qué es: Es un patrón de diseño estructural que permite componer
objetos en estructuras de árbol y luego trabajar con esas
estructuras como si fueran un objeto individual.

Cuándo usarlo: Cuando necesitas representar una jerarquía
parte-todo (como carpetas que contienen archivos y otras
carpetas), y quieres que el cliente trate los elementos
individuales (hojas) y los contenedores (compuestos) de la
misma manera, sin distinguir entre ellos.

Para qué: Simplificar el código cliente, que puede recorrer u
operar sobre toda la estructura del árbol a través de una sola
interfaz común, sin condicionales que distingan si un elemento
es simple o compuesto.

Ejemplo del patrón Composite: sistema de archivos.

Carpeta puede contener tanto Archivos (hojas) como otras
Carpetas (compuestos), y el cliente llama a mostrar() sobre
la carpeta principal sin saber qué tan profundo es el árbol.
"""

from abc import ABC, abstractmethod


# Componente abstracto
class ComponenteArchivo(ABC):
    @abstractmethod
    def mostrar(self, nivel: int = 0) -> None: ...


# Hoja
class Archivo(ComponenteArchivo):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar(self, nivel: int = 0) -> None:
        print(" " * nivel + f"Archivo: {self.nombre}")


# Compuesto
class Carpeta(ComponenteArchivo):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.contenido: list[ComponenteArchivo] = []

    def agregar(self, componente: ComponenteArchivo) -> None:
        self.contenido.append(componente)

    def mostrar(self, nivel: int = 0) -> None:
        print(" " * nivel + f"Carpeta: {self.nombre}")
        for componente in self.contenido:
            componente.mostrar(nivel + 1)


# Cliente: solo llama a mostrar() sobre la raíz,
# sin preocuparse por la profundidad del árbol
if __name__ == "__main__":
    archivo1 = Archivo("documento1.txt")
    archivo2 = Archivo("imagen1.png")
    archivo3 = Archivo("video1.mp4")

    carpeta_principal = Carpeta("Carpeta Principal")
    subcarpeta1 = Carpeta("Subcarpeta 1")
    subcarpeta2 = Carpeta("Subcarpeta 2")

    carpeta_principal.agregar(archivo1)
    subcarpeta1.agregar(archivo2)
    subcarpeta2.agregar(archivo3)

    carpeta_principal.agregar(subcarpeta1)
    carpeta_principal.agregar(subcarpeta2)

    carpeta_principal.mostrar()
