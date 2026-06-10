"""
Gestor de archivos con DIP
Las clases de alto nivel no deben depender de clases de bajo nivel.
Ambas deben depender de abstracciones (interfaces o clases abstractas).
"""

from abc import ABC, abstractmethod


# ✅ Abstracción — ni alto ni bajo nivel dependen entre sí, ambos dependen de esto
class Readable(ABC):
    @abstractmethod
    def read(self, filename: str) -> str:
        pass


# ✅ Bajo nivel — implementaciones concretas
class LocalStorage(Readable):
    def read(self, filename: str) -> str:
        return f"[LOCAL] Leyendo archivo: {filename}"


class AWSS3Storage(Readable):
    def read(self, filename: str) -> str:
        return f"[AWS S3] Descargando archivo: {filename}"


class DatabaseStorage(Readable):
    def read(self, filename: str) -> str:
        return f"[DATABASE] Consultando registro: {filename}"


# ✅ Alto nivel — depende de la abstracción, NO de las clases concretas
class FileManager:
    def __init__(self, storage: Readable):  # 👈 Recibe la abstracción
        self.storage = storage

    def open_file(self, filename: str) -> str:
        return self.storage.read(filename)


# Uso — inyectamos la dependencia desde afuera
manager = FileManager(LocalStorage())
print(manager.open_file("factura.pdf"))

manager = FileManager(AWSS3Storage())
print(manager.open_file("reporte.csv"))

manager = FileManager(DatabaseStorage())
print(manager.open_file("cliente_01"))
