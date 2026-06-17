"""
Patrón Bridge

Qué es: Es un patrón de diseño estructural que permite separar
una abstracción de su implementación, de modo que ambas puedan
variar de forma independiente.

Cuándo usarlo: Cuando tienes una abstracción que puede tener
varias implementaciones (o viceversa), y quieres evitar una
explosión combinatoria de subclases para cada combinación
posible (por ejemplo, InformePDF, InformeWord, ResumenPDF,
ResumenWord...), o cuando necesitas poder cambiar la
implementación en tiempo de ejecución.

Para qué: Desacoplar la abstracción de la implementación, de
forma que ambas jerarquías de clases evolucionen por separado,
sin que un cambio en una obligue a modificar la otra.

Ejemplo del patrón Bridge: sistema de generación de documentos
en distintos formatos.

Documento (la abstracción) y FormatoDocumento (la implementación)
varían de forma independiente: agregar un nuevo tipo de documento
(por ejemplo, InformeResumen) o un nuevo formato (por ejemplo,
FormatoExcel) no requiere tocar la otra jerarquía.
"""

from abc import ABC, abstractmethod


# Implementación: interfaz de formatos
class FormatoDocumento(ABC):
    @abstractmethod
    def generar(self, contenido: str) -> None: ...


# Implementaciones concretas
class FormatoPDF(FormatoDocumento):
    def generar(self, contenido: str) -> None:
        print(f"Generando PDF con el contenido: {contenido}")


class FormatoWord(FormatoDocumento):
    def generar(self, contenido: str) -> None:
        print(f"Generando Word con el contenido: {contenido}")


# Abstracción: usa un FormatoDocumento internamente (el "puente")
class Documento:
    def __init__(self, formato: FormatoDocumento):
        self.formato = formato

    def generar(self, contenido: str) -> None:
        self.formato.generar(contenido)


# Cliente
if __name__ == "__main__":
    documento_pdf = Documento(FormatoPDF())
    documento_pdf.generar("Informe Financiero")

    documento_word = Documento(FormatoWord())
    documento_word.generar("Informe de Ventas")
