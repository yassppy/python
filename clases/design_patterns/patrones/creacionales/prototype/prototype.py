"""
PATRÓN PROTOTYPE: Clonas un objeto existente en lugar de crear uno nuevo desde cero.
Es útil cuando crear un objeto desde cero es costoso en tiempo o recursos.

- copy.copy (copia superficial): Copia los atributos simples de forma independiente,
  pero los objetos anidados como Address se comparten con el original.
  Si modificas el objeto anidado en la copia, también se modifica en el original.

- copy.deepcopy (copia profunda): Copia todo de forma completamente independiente,
  incluidos los objetos anidados. Modificar la copia no afecta al original.

Regla: Si tu objeto tiene objetos anidados, usa siempre copy.deepcopy.
"""

import copy


class Person:
    """clase persona que queremos clonar"""

    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        return f"Nombre: {self.name}, Edad: {self.age}, Dirección: {self.address}"


class Address:
    """clase address para mostrar"""

    def __init__(self, street, city) -> None:
        self.street = street
        self.city = city

    def __str__(self) -> str:
        return f"Street: {self.street}, City: {self.city}"


if __name__ == "__main__":
    address = Address("123 Main St", "Anytown")
    person = Person("John Doe", 30, address)

    person2 = copy.copy(person)  # clon superficial
    person3 = copy.deepcopy(person)  # clon profundo

    # 👇 Aquí se ve la diferencia real
    person2.address.street = "456 Other St"  # modificas el clon superficial
    person3.address.street = "789 Another St"  # modificas el clon profundo

    print(f"Original:         {person}")  # 😱 cambió por person2
    print(f"Clon superficial: {person2}")
    print(f"Clon profundo:    {person3}")  # ✅ no afectó al original
