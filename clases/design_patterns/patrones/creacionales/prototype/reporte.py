"""
1. ConfigManager: mantenga y lea parametros como url de la bd, nivel de logging y la clave API. Debe existir una
unica instancia de ConfigManager que sea compartida por toda la aplicacion.
2. Un sistema de plantillas de reporte (ReportTemplate) que permita clonar una estructura
encabezado, pie de página, estilos, datos por defecto rápido para generar reportes especificos sin volver a iniciar
una nueva plantilla desde cero.

En el primero caso aplicamos el patrón singlenton
En el segundo caso utilizamos el patrón prototype
"""

import copy


class ConfigManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Evitar inicializar toda la instancia"""
        if getattr(self, "_initialized", False):
            return

        self._initialized = True
        self._url = "sqlite:///app.db"
        self._log_level = "INFO"
        self._api_key = "DEV-KEY-001"

    def get_config(self, key):
        return getattr(self, key, None)

    def set_config(self, key, value):
        return setattr(self, key, value)


class ReportTemplate:
    def __init__(self, title, header, footer, data=None) -> None:
        self.title = title
        self.header = header
        self.footer = footer
        self.data = data or {}

    def add_section(self, section_name, content):
        """Modificar el contenido de un reporte"""
        self.data[section_name] = content

    def clone(self):
        """Retorna una copia totalmente independiente del reporte"""
        return copy.deepcopy(self)


if __name__ == "__main__":
    print("=" * 40)
    print("Ejemplo de uso del patrón SINGLETON")
    cfg1 = ConfigManager()
    cfg2 = ConfigManager()
    cfg3 = ConfigManager()
    print(f"misma instancia: {cfg1 is cfg2}")
    print(f"nivel de log: {cfg2.get_config('_log_level')}")
    cfg2.set_config("_log_level", "DEBUG")
    print(f"nivel de log: {cfg2.get_config('_log_level')}")

    print("=" * 40)
    print("Ejemplo de uso del patrón PROTOTYPE")
    plantilla_base = ReportTemplate(
        title="Reporte Mensual",
        header="Empresa S.A.",
        footer="Confidencial",
        data={"ventas": 1000, "detalle": ["enero", "febrero"]},
    )
    print(f"id(plantilla_base) = {id(plantilla_base)}")
    print(f"id(plantilla_base.data) = {id(plantilla_base.data)}")

    reporte_clon = plantilla_base.clone()
    print(f"id(reporte_clon) = {id(reporte_clon)}")
    print(f"id(reporte_clon.data) = {id(reporte_clon.data)}")
    print(
        f"¿Es el mismo objeto? (plantilla_base is reporte_clon) -> "
        f"{plantilla_base is reporte_clon}"
    )
    print(
        f"¿Comparten el mismo diccionario 'data'? -> "
        f"{plantilla_base.data is reporte_clon.data}"
    )

    # Modificamos SOLO el clon, incluyendo una lista anidada dentro de data
    reporte_clon.title = "Reporte Clonado - Enero"
    reporte_clon.add_section("gastos", 500)
    reporte_clon.data["detalle"].append("marzo")

    print("\n--- Después de modificar únicamente el CLON ---")
    print(f"Clon     -> título: {reporte_clon.title}")
    print(f"Clon     -> data:   {reporte_clon.data}")
    print(f"Original -> título: {plantilla_base.title}")
    print(f"Original -> data:   {plantilla_base.data}")

    print("\n¿El original se vio afectado por los cambios del clon?")
    if plantilla_base.data == reporte_clon.data:
        print("   Sí (esto indicaría un error: faltaría deepcopy)")
    else:
        print("   No, el original permanece intacto gracias a copy.deepcopy()")
