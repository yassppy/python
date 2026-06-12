"""
1. ConfigManager: mantenga y lea parametros como url de la bd, nivel de logging y la clave API. Debe existir una
unica instancia de ConfigManager que sea compartida por toda la aplicacion.
2. Un sistema de plantillas de reporte (ReportTemplate) que permita clonar una estructura
encabezado, pie de página, estilos, datos por defecto rápido para generar reportes especificos sin volver a iniciar
una nueva plantilla desde cero.

En el primero caso aplicamos el patrón singlenton
En el segundo caso utilizamos el patrón prototype
"""


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
    def __init__(self) -> None:
        pass
