# Principios SOLID en Programación Orientada a Objetos

Los principios SOLID son reglas de diseño que ayudan a crear código:

- Escalable → fácil de ampliar.
- Flexible → fácil de modificar.
- Entendible → otros programadores pueden comprenderlo.
- Mantenible → corregir errores o agregar funciones cuesta menos esfuerzo.

El objetivo no es seguirlos como reglas absolutas, sino tomar mejores decisiones al programar.

```
__str__() solo decide:
```
"¿Cómo quiero que el objeto se vea cuando alguien lo imprima?"
Es como poner una etiqueta bonita a una caja; el contenido interno no cambia.

---

# 1. Principio de Responsabilidad Única (SRP)

## Idea principal

Una clase debe tener una sola responsabilidad o ``motivo para cambiar``.

Si una clase hace demasiadas cosas:

- Es difícil de entender.
- Es difícil mantenerla.
- Un cambio puede romper otras funcionalidades.

## Ejemplo de la vida real

Piensa en un restaurante:

Una persona:

- cocina
- cobra
- recibe pedidos
- limpia mesas

Eso genera problemas.

Lo correcto sería:

- Cocinero → cocina
- Cajero → cobra
- Mesero → recibe pedidos

Cada uno tiene una única responsabilidad.

---

## Ejemplo incorrecto

```python
class Usuario:

    def guardar_usuario(self):
        print("Guardando usuario")

    def enviar_correo(self):
        print("Enviando correo")

    def generar_reporte(self):
        print("Generando reporte")
```

Problema:

La clase hace demasiadas cosas.

---

## Ejemplo correcto

```python
class Usuario:
    def guardar_usuario(self):
        print("Guardando usuario")


class ServicioCorreo:
    def enviar_correo(self):
        print("Enviando correo")


class Reporte:
    def generar_reporte(self):
        print("Generando reporte")
```

Cada clase tiene una sola responsabilidad.

---

# 2. Principio Abierto/Cerrado (OCP)

## Idea principal

Las clases deben:

Abiertas para extensión -> Agregar nuevas funcionalidades.
Cerradas para modificación -> No necesito tocar el código cada rato a las funcionalidades ya creadas.

Es decir:

Puedo agregar nuevas funcionalidades sin modificar el código existente.

---

## Ejemplo de la vida real

Una aplicación de pagos:

Inicialmente:

- Tarjeta

Luego agregan:

- PayPal
- Yape
- Criptomonedas

No debería modificarse todo el sistema cada vez.

---

## Ejemplo incorrecto

```python
class Pago:

    def procesar(self,tipo):

        if tipo=="tarjeta":
            print("Pago con tarjeta")

        elif tipo=="paypal":
            print("Pago con paypal")
```

Problema:

Cada nuevo método obliga a modificar la clase.

---

## Ejemplo correcto

```python
from abc import ABC, abstractmethod

class MetodoPago(ABC):

    @abstractmethod
    def pagar(self):
        pass


class Tarjeta(MetodoPago):

    def pagar(self):
        print("Pago con tarjeta")


class Paypal(MetodoPago):

    def pagar(self):
        print("Pago con Paypal")
```

Uso:

```python
pago=Tarjeta()
pago.pagar()
```

Para agregar otro método solo creamos otra clase.

---

# 3. Principio de Sustitución de Liskov (LSP)

## Idea principal

Una clase hija debe poder reemplazar a su clase padre sin romper el programa.

LSP significa que las subclases deben comportarse como su padre, sin sorpresas ni contradicciones.

---

## Ejemplo de la vida real

Clase padre:

Vehículo

Clases hijas:

- Auto
- Moto

Si una función espera un vehículo, debería aceptar cualquiera sin problemas.

---

## Ejemplo incorrecto

```python
class Ave:

    def volar(self):
        print("Volando")


class Pinguino(Ave):

    def volar(self):
        raise Exception("No puedo volar")
```

Problema:

Un pingüino no puede reemplazar correctamente a Ave.

---

## Ejemplo correcto

```python
class Ave:
    pass


class AveVoladora(Ave):

    def volar(self):
        print("Volando")


class Pinguino(Ave):
    pass


class Aguila(AveVoladora):
    pass
```

Ahora no rompemos el comportamiento esperado.

---

# 4. Principio de Segregación de Interfaces (ISP)

## Idea principal

No obligar a una clase a implementar métodos que no necesita.

Es mejor tener varias interfaces pequeñas que una enorme.

---

## Ejemplo de la vida real

Un trabajador:

No todos:

- cocinan
- cobran
- limpian

Cada trabajador debería implementar solo lo que necesita.

---

## Ejemplo incorrecto

```python
class Trabajador:

    def cocinar(self):
        pass

    def cobrar(self):
        pass

    def programar(self):
        pass
```

Un programador tendría que implementar cocinar y cobrar aunque no los use.

---

## Ejemplo correcto

```python
class Cocinero:

    def cocinar(self):
        pass


class Cajero:

    def cobrar(self):
        pass


class Programador:

    def programar(self):
        pass
```

Cada uno implementa únicamente lo necesario.

---

# 5. Principio de Inversión de Dependencias (DIP)

## Idea principal

Los módulos de alto nivel y bajo nivel deben depender de abstracciones y no directamente entre ellos.

El Principio de Inversión de Dependencias asegura que las piezas importantes de tu sistema dependan de reglas generales (abstracciones) y no de detalles específicos. Así puedes cambiar las partes internas sin romper el resto del programa.

---

## Explicación simple

Imagínate:

Una computadora usa:

- teclado Logitech
- teclado Redragon
- teclado HP

La computadora no debería depender de una marca específica.

Debe depender de algo general:

"Teclado"

---

## Ejemplo incorrecto

```python
class MySQL:

    def conectar(self):
        print("Conectando MySQL")


class Aplicacion:

    def __init__(self):
        self.db=MySQL()
```

Problema:

La aplicación depende directamente de MySQL.

Si cambias a PostgreSQL debes modificar el código.

---

## Ejemplo correcto

```python
from abc import ABC, abstractmethod

class BaseDatos(ABC):

    @abstractmethod
    def conectar(self):
        pass


class MySQL(BaseDatos):

    def conectar(self):
        print("Conectando MySQL")


class PostgreSQL(BaseDatos):

    def conectar(self):
        print("Conectando PostgreSQL")


class Aplicacion:

    def __init__(self,db):
        self.db=db
```

Uso:

```python
db=MySQL()

app=Aplicacion(db)
```

Si mañana cambias:

```python
db=PostgreSQL()
```

No modificas la aplicación.

---

# Frase para memorizar SOLID

S → Una clase con una única responsabilidad
O → Extender nuevas funcionalidades pero sin modificar el resto del código existente.
L → Mi subclases sustituyen el comportamiento esperado
I → Interfaces pequeñas para implementar lo que se necesita
D → Depender de abstracciones ante las diversas formas en que uno se puede conectar (Base de datos, Modelos, etc)
