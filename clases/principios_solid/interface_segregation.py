# Como en el caso anterior no hay que obligar a las clases a implementar métodos que no necesita.
# Por ejemplo, las funcionalidades de trabajadores de una empresa
# Esto complementa lo de liskov con metodos abstractos

from abc import ABC, abstractmethod

class ProgrammerRole(ABC):
    @abstractmethod
    def program(self):
        pass

class CookRole(ABC):
    @abstractmethod
    def cook(self):
        pass

class DriverRole(ABC):
    @abstractmethod
    def drive(self):
        pass

class Programmer(ProgrammerRole):
    def program(self):
        print("Automatizando pedidos")

class Chef(CookRole):
    def cook(self):
        print("Cocinando Pedido")

programmer = Programmer()
programmer.program()