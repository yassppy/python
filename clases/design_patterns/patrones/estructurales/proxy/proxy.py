"""
Patrón Proxy

Qué es: Es un patrón de diseño estructural que proporciona un
sustituto o representante de otro objeto, controlando el acceso
a él.

Cuándo usarlo: Cuando necesitas controlar el acceso a un objeto,
por ejemplo validando permisos antes de delegar la llamada,
limitando el número de solicitudes, o retrasando la creación de
un objeto costoso hasta que realmente se necesite.

Para qué: Añadir lógica de control (autenticación, límite de uso,
caché, registro, etc.) sin modificar el objeto real ni el código
cliente, ya que ambos comparten la misma interfaz y el cliente no
distingue si está hablando con el proxy o con el objeto real.

Ejemplo del patrón Proxy: control de acceso a una API externa.

ProxyAPI se interpone entre el cliente y APIReal para:
1. Verificar que el token de autenticación sea válido.
2. Limitar el número de solicitudes permitidas en un periodo de
   tiempo (1 minuto en este ejemplo).

Solo si ambas condiciones se cumplen, el proxy delega la
llamada a la API real.
"""

import time
from abc import ABC, abstractmethod


# Interfaz para la API
class API(ABC):
    @abstractmethod
    def solicitar_datos(self) -> str: ...


# Clase que representa la API real
class APIReal(API):
    def solicitar_datos(self) -> str:
        return "Datos importantes de la API real"


# Proxy de la API
class ProxyAPI(API):
    def __init__(self, token: str):
        self._api_real = APIReal()
        self._token = token
        self._limite_solicitudes = 5  # Número máximo de solicitudes permitido
        self._contador_solicitudes = 0
        self._ultima_llamada = time.time()  # Marca de tiempo de la última llamada

    def solicitar_datos(self) -> str:
        if not self._verificar_token():
            return "Error: Token de autenticación no válido."

        if not self._verificar_limite_solicitudes():
            return "Error: Límite de solicitudes alcanzado. Inténtelo más tarde."

        # Actualizamos el contador y el tiempo de la última llamada
        self._contador_solicitudes += 1
        self._ultima_llamada = time.time()

        return self._api_real.solicitar_datos()

    def _verificar_token(self) -> bool:
        # Verificación del token de autenticación
        print("Proxy: Verificando el token...")
        return self._token == "TOKEN_VALIDO"

    def _verificar_limite_solicitudes(self) -> bool:
        # Reinicia el contador si ha pasado suficiente tiempo (por ejemplo, 1 minuto)
        if time.time() - self._ultima_llamada > 60:
            self._contador_solicitudes = 0
        return self._contador_solicitudes < self._limite_solicitudes


# Cliente que usa el proxy para interactuar con la API
def cliente(proxy: API) -> None:
    for _ in range(7):  # Intentamos más de 5 solicitudes para probar el límite
        print(proxy.solicitar_datos())
        time.sleep(1)  # Espera de 1 segundo entre solicitudes


if __name__ == "__main__":
    print("Cliente: Intentando acceder a la API mediante el proxy.")
    proxy = ProxyAPI("TOKEN_VALIDO")  # Usamos un token correcto
    cliente(proxy)

    # Para ver el comportamiento sin el token correcto, descomenta:
    # proxy_invalido = ProxyAPI("TOKEN_INVALIDO")
    # cliente(proxy_invalido)
