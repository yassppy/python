"""
Manejar una conexión de base de datos con
singlenton solo crear una instancia única para evitar múltiples conexiones simultáneas.
"""

import time


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        if not self.connected:
            print("Conectando a la base de datos...")
            time.sleep(1)
            self.connected = True
            print("Conexión establecida.")
        else:
            print("Ya estás conectado a la base de datos.")

    def execute_query(self, query):
        if self.connected:
            print(f"Ejecutando consulta: {query}")
            time.sleep(0.5)
            print(f"Consulta '{query}' ejecutada con éxito.")
        else:
            print("No se puede ejecutar la consulta. Conéctate primero.")

    def disconnect(self):
        if self.connected:
            print("Cerrando la conexión...")
            time.sleep(1)
            self.connected = False
            print("Conexión cerrada.")
        else:
            print("No hay ninguna conexión activa.")


if __name__ == "__main__":
    db1 = DatabaseConnection()

    db1.connect()

    db1.execute_query("SELECT * FROM customers")

    db2 = DatabaseConnection()
    print(db1 is db2)

    db2.execute_query("SELECT * FROM orders")
