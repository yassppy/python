class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = nueva_edad

    def hablar(self):
        return "..."


class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


# Uso
perro = Perro("Rex", 8)
gato = Gato("Luna", 4)

print(perro.hablar())
print(gato.hablar())