"""
Gestor de archivos va a leer diferentes tipos de almacenamiento (local, nube de aws s3, base de datos)
El sistema debe ser flexible para agregar nuevos métodos de almacenamiento sin modificar el
código existente y evitar que las clases dependan de funcionalidades que no usan.

Se aplicara el principio de segregación de interfaces (ISP) no hay que obligar a las clases a implementar
métodos de una interfaz que no usan.
"""

from abc import ABC, abstractmethod


# ✅ Interfaces pequeñas y específicas, cada una con su responsabilidad
class Readable(ABC):
    @abstractmethod
    def read(self, filename: str) -> str:
        pass


class Writable(ABC):
    @abstractmethod
    def write(self, filename: str, data: str) -> None:
        pass


class Deletable(ABC):
    @abstractmethod
    def delete(self, filename: str) -> None:
        pass


# ✅ cada clase hereda lo que necesita
class LocalStorage(Readable, Writable, Deletable):
    def read(self, filename: str) -> str:
        return f"[LOCAL] Leyendo archivo: {filename}"

    def write(self, filename: str, data: str) -> None:
        print(f"[LOCAL] Guardando '{data}' en {filename}")

    def delete(self, filename: str) -> None:
        print(f"[LOCAL] Eliminando archivo: {filename}")


# ✅ AWS S3 solo lee y escribe, NO elimina directamente
class AWSS3Storage(Readable, Writable):
    def read(self, filename: str) -> str:
        return f"[AWS S3] Descargando archivo: {filename}"

    def write(self, filename: str, data: str) -> None:
        print(f"[AWS S3] Subiendo '{data}' a {filename}")


# ✅ Base de datos solo lee, NO escribe ni elimina archivos
class DatabaseStorage(Readable):
    def read(self, filename: str) -> str:
        return f"[DATABASE] Consultando registro: {filename}"


# Uso
local = LocalStorage()
s3 = AWSS3Storage()
db = DatabaseStorage()

# Local
print(local.read("factura.pdf"))
local.write("factura.pdf", "data de factura")
local.delete("factura.pdf")
print("---")

# AWS S3
print(s3.read("reporte.csv"))
s3.write("reporte.csv", "data del reporte")
print("---")

# Base de datos
print(db.read("cliente_01"))
