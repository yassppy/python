"""
Principio de responsabilidad única (SRP): Una clase debe tener una única responsabilidad.
"""


class OrderCalculator:
    """Responsable de calcular el pedido"""

    def calculate(self, price: float, quantity: int) -> float:
        return price * quantity

    def calculate_igv(self, total: float) -> float:
        return total * 0.18

    def calculate_total(self, subtotal: float, igv: float) -> float:
        return subtotal + igv


class InvoicePrinter:
    """Responsable de imprimir la factura"""

    def print_invoice(self, subtotal: float, igv: float, total: float) -> None:
        print(f"Subtotal: {subtotal}")
        print(f"IGV: {igv}")
        print(f"Total: {total}")


calculator = OrderCalculator()
printer = InvoicePrinter()

subtotal = calculator.calculate(100, 5)
igv = calculator.calculate_igv(subtotal)
total = calculator.calculate_total(subtotal, igv)
printer.print_invoice(subtotal, igv, total)
