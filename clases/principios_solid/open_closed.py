from abc import ABC, abstractmethod

# Un GYM que tiene descuentos por tipo de clientes, la idea no es poner todo en un metodo
# ya que si agrego nuevas reglas voy a estar modificando la función cada rato.
# Por eso la clase abstracta ya que nos permite heredar la clase e importar si o si su metodo.
# Con esto cumplimos el principio de abierto para nuevas funcionalidades y cerrado para modificaciones

class Discount(ABC):

    @abstractmethod
    def calculate(self):
        pass

class GoldDiscount(Discount):
    def calculate(self):
        return 0.20

class SilverDiscount(Discount):
    def calculate(self):
        return 0.10
    
gold = GoldDiscount()
silver = SilverDiscount()

print(gold.calculate())
print(silver.calculate())