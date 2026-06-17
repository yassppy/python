"""
Ejemplo del patrón Facade aplicado a un restaurante.

Subsistemas:
- Cocina
- ServicioMesas
- SistemaFacturacion

La clase RestauranteFacade coordina estos tres subsistemas
para que el cliente no tenga que interactuar con cada uno
por separado.
"""


class Cocina:
    def comenzar_preparacion(self, plato):
        print(f"[Cocina] Comenzando preparación de: {plato}")

    def terminar_preparacion(self, plato):
        print(f"[Cocina] Preparación de {plato} terminada")


class ServicioMesas:
    def asignar_mesa(self, cliente):
        print(f"[Servicio de mesas] Mesa asignada a {cliente}")

    def servir_plato(self, plato, cliente):
        print(f"[Servicio de mesas] Sirviendo {plato} a {cliente}")


class SistemaFacturacion:
    def generar_factura(self, cliente, monto):
        print(f"[Facturación] Factura generada para {cliente}: ${monto}")

    def pagar_factura(self, cliente):
        print(f"[Facturación] {cliente} ha pagado la factura")


class RestauranteFacade:
    def __init__(self):
        self.cocina = Cocina()
        self.servicio_mesas = ServicioMesas()
        self.facturacion = SistemaFacturacion()

    def recibir_orden(self, cliente, plato):
        """Coordina cocina, servicio de mesa y el inicio de la orden."""
        print(f"\n--- Nueva orden de {cliente}: {plato} ---")
        self.servicio_mesas.asignar_mesa(cliente)
        self.cocina.comenzar_preparacion(plato)

    def completar_orden(self, cliente, plato, monto):
        """Termina el ciclo: cocina prepara, mesa sirve, cliente paga."""
        self.cocina.terminar_preparacion(plato)
        self.servicio_mesas.servir_plato(plato, cliente)
        self.facturacion.generar_factura(cliente, monto)
        self.facturacion.pagar_factura(cliente)
        print(f"--- Orden de {cliente} completada ---\n")


# Cliente: solo interactúa con la Facade
if __name__ == "__main__":
    restaurante = RestauranteFacade()

    restaurante.recibir_orden("Ana", "Lomo saltado")
    restaurante.completar_orden("Ana", "Lomo saltado", 25.50)
