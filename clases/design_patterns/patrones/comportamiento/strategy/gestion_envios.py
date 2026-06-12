"""
Gestión de Envíos en una Tienda en Línea
utilizando el PATRÓN STRATEGY: Permite definir una familia de algoritmos, colocando cada uno de las clases
separadas y hace que sus objetos sean intercambiables.

Caso:
La tienda ofrece envíos a tres países: Estados Unidos, Canadá y Brasil. El cálculo de los costos de envío
se realiza de la siguiente forma:
Estados Unidos: El costo de envío es una tarifa fija de $10 más un porcentaje del precio del producto (5%).
Canada: El costo de envío depende del peso del producto. Se cobra $1 por cada kilogramo de peso.
Brasil: El costo de envío es una tarifa fija de $15, sin importar el precio ni el peso del producto.
"""

from abc import ABC, abstractmethod


# Estrategia de comportamientos intercambiables
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping_cost(
        self, product_price: float, product_weight: float
    ) -> float:
        return 0.0


class ShippingStrategyUS(ShippingStrategy):
    def calculate_shipping_cost(
        self, product_price: float, product_weight: float
    ) -> float:
        fixed_rate = 10
        return fixed_rate + product_price * 0.05


class ShippingStrategyCanada(ShippingStrategy):
    def calculate_shipping_cost(
        self, product_price: float, product_weight: float
    ) -> float:
        price_per_kilogram = 1
        return product_weight * price_per_kilogram


class ShippingStrategyBrazil(ShippingStrategy):
    def calculate_shipping_cost(
        self, product_price: float, product_weight: float
    ) -> float:
        fixed_rate = 15
        return fixed_rate


## Donde se referencia la estrategia y comportamiento
class ShippingManager:
    def __init__(self, shipping_strategy: ShippingStrategy) -> None:
        self.shipping_strategy = shipping_strategy

    def calculate_total(
        self,
        product_price: float,
        product_weight: float,
    ) -> float:
        shipping_cost = self.shipping_strategy.calculate_shipping_cost(
            product_price, product_weight
        )
        return product_price + shipping_cost


product_price = 1000.0
product_weight = 2.0

shipping_manager_us = ShippingManager(ShippingStrategyUS())
shipping_manager_ca = ShippingManager(ShippingStrategyCanada())
shipping_manager_br = ShippingManager(ShippingStrategyBrazil())

print(
    f"USA    → ${shipping_manager_us.calculate_total(product_price, product_weight):.2f}"
)
print(
    f"Canada → ${shipping_manager_ca.calculate_total(product_price, product_weight):.2f}"
)
print(
    f"Brazil → ${shipping_manager_br.calculate_total(product_price, product_weight):.2f}"
)

# USA    → $1060.00  (1000 + 10 + 50)
# Canada → $1002.00  (1000 + 2*1)
# Brazil → $1015.00  (1000 + 15)
