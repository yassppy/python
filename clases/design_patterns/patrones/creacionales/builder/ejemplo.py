"""
El patrón BUILDER nos permite construir objetos complejos paso a paso.
Separa la consturcción de un objeto de su representación permitiendo crear diferentes
tipos de representaciones del mismo objeto.

Ejemplo: construir un sándwich
Teniendo un constructor paso a paso que permita agregar ingredientes al sándwich de manera controlada.
"""


class Sandwich:
    def __init__(self):
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar_ingredientes(self):
        return f"Sándwich con {', '.join(self.ingredientes)}"


class SandwichBuilder:
    """Se va a encargar de agregar diferentes ingredientes"""

    def __init__(self):
        self.sandwich = Sandwich()

    def agregar_hamburguesa(self):
        self.sandwich.agregar_ingrediente("hamburguesa")

    def agregar_pan(self):
        self.sandwich.agregar_ingrediente("pan")

    def agregar_queso(self):
        self.sandwich.agregar_ingrediente("queso")

    def agregar_vegetales(self):
        self.sandwich.agregar_ingrediente("vegetales")

    def build(self):
        sandwich_terminado = self.sandwich
        self.sandwich = Sandwich()
        return sandwich_terminado


## Director opcional
class DirectorSandwich:
    """El director se encarga  de utilizar el builder para construir un objeto en especifico"""

    def __init__(self, builder):
        self.builder = builder

    def construir_sandwich_clasico(self):
        self.builder.agregar_pan()
        self.builder.agregar_queso()
        self.builder.agregar_hamburguesa()
        self.builder.agregar_vegetales()
        return self.builder.build()

    def construir_sandwich_vegetariano(self):
        self.builder.agregar_pan()
        self.builder.agregar_vegetales()
        self.builder.agregar_queso()
        return self.builder.build()


if __name__ == "__main__":
    builder = SandwichBuilder()
    director = DirectorSandwich(builder)
    # crear sandwiche clasico
    sandwich_clasico = director.construir_sandwich_clasico()
    # crear sandwiche vegetariano
    sandwich_vegetariano = director.construir_sandwich_vegetariano()
    print(sandwich_clasico.mostrar_ingredientes())
    print(sandwich_vegetariano.mostrar_ingredientes())
