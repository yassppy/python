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
    
    def info(self):
        return f"Nombre Animal: {self.nombre}, Edad Animal: {self.edad}"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad) # Inicializar los valores cuando lo instancio
        self.raza = raza

    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

perro = Perro("Rex", 5, "Labrador")

print(f"Mi perro se llama {perro.nombre}")
print(f"Mi perro es de raza {perro.raza}")
print(f"Mi perro tiene {perro.edad} años")
perro.edad = 15
print(f"\nEsta es la información de mi perro \n{perro.info()}")