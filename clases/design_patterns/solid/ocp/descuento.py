"""
Consutir una aplicación de descuentos

Principio abierto y cerrado (OCP)
Abiertas para extensión -> Agregar nuevas funcionalidades como otros tipos de descuentos.
Cerradas para modificación -> No tocamos el código existente.
"""

from abc import ABC, abstractmethod


class Discount(ABC):
    """Clase abstracta para descuentos"""

    @abstractmethod
    def calculate(self, monto: float) -> float:
        """Decorador y función abstracto para calcular el descuento"""
        pass


class RegularDiscount(Discount):
    def calculate(self, monto: float) -> float:
        return monto * 0.10


class PremiumDiscount(Discount):
    def calculate(self, monto: float) -> float:
        return monto * 0.20


class VipDiscount(Discount):
    def calculate(self, monto: float) -> float:
        return monto * 0.30


def apply_discount(discount: Discount, monto: float) -> float:
    discount_amount = discount.calculate(monto)
    total = monto - discount_amount
    return total


cash = 1000
discount = RegularDiscount()
result = apply_discount(discount, cash)
print(result)
