"""
Patrón Singleton con decorador, mantiene un diccionario de instancias
si ya existe una instancia de la clase, devuelve la misma instancia
si no existe, crea una nueva instancia y la almacena en el diccionario
"""


def Singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@Singleton
class MyClass:
    def __init__(self):
        self.value = 42


# Probando el pratrón con decorador
singlenton1 = MyClass()
singlenton2 = MyClass()

print(singlenton1 is singlenton2)
