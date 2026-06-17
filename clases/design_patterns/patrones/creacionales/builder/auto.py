"""
Builder: el objeto debe ser construido paso por paso agregando diferentes partes
Ejemplo Automóvil agregar partes como motor, ruedas, color, sistema de entretenimiento
"""


class Auto:
    def __init__(self):
        self.tipo_motor = ""
        self.numero_ruedas = 4
        self.color = ""
        self.sistema_de_entretenimiento = False

    def mostrar(self):
        print("=" * 10)
        print("Automóvil construido")
        print(f"Tipo motor: {self.tipo_motor}")
        print(f"Ruedas: {self.numero_ruedas}")
        print(f"Color: {self.color}")
        estado_entretenimiento = "Si" if self.sistema_de_entretenimiento else "No"
        print(f"Sistema de entretenimiento: {estado_entretenimiento}")


class AutomovilBuilder:
    """Permite construir el objeto automóvil paso a paso"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.auto = Auto()

    def set_tipo_motor(self, tipo_motor):
        self.auto.tipo_motor = tipo_motor
        return self

    def set_numero_ruedas(self, numero_ruedas):
        self.auto.numero_ruedas = numero_ruedas
        return self

    def set_color(self, color):
        self.auto.color = color
        return self

    def set_sistema_de_entretenimiento(self, sistema_de_entretenimiento):
        self.auto.sistema_de_entretenimiento = sistema_de_entretenimiento
        return self

    def build(self):
        auto_terminado = self.auto
        self.reset()
        return auto_terminado


class DirectorAutomovil:
    """Construye automóviles específicos utilizando un builder"""

    def __init__(self, builder):
        self.builder = builder

    def construir_auto_lujo(self):
        self.builder.set_tipo_motor("V8")
        self.builder.set_numero_ruedas(4)
        self.builder.set_color("Negro")
        self.builder.set_sistema_de_entretenimiento(True)
        return self.builder.build()

    def construir_auto_medio(self):
        self.builder.set_tipo_motor("V6")
        self.builder.set_numero_ruedas(4)
        self.builder.set_color("Blanco")
        self.builder.set_sistema_de_entretenimiento(False)
        return self.builder.build()


if __name__ == "__main__":
    director = DirectorAutomovil(AutomovilBuilder())
    auto_lujo = director.construir_auto_lujo()
    auto_medio = director.construir_auto_medio()
    auto_lujo.mostrar()
    auto_medio.mostrar()
