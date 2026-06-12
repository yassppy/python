"""
Con singlenton solamente creamos una instancia única de la clase.

Primero tiene que existir la casa (__new__)  construyendo el objeto
para luego decorarla (__init__) inicializando el objeto.
"""


class Singlenton:
    _instance = None

    def __new__(cls):
        """Crea el objeto antes de que exista"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Construye una sola vez
        return cls._instance


# Probando el patrón Singlenton
singlenton1 = Singlenton()
singlenton2 = Singlenton()

print(singlenton1 is singlenton2)
