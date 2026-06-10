"""
Ejercicio de modelar figuras geométricas para calcular su área

Aplicando el principio de sustitución de Liskov (LSP)
"""

import math


class Figura:
    def area(self) -> float:
        return 0


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return round(self.base * self.altura, 2)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * self.radio**2, 2)


def imprimir_area(figura: Figura):
    print(f"Area: {figura.area()}")


imprimir_area(Circulo(3))
imprimir_area(Rectangulo(3, 4))
