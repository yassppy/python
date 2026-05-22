# Funciones en Python — Episodio 9

## Funciones: conceptos básicos

Una función es un bloque de código reutilizable que encapsula instrucciones y puede recibir datos (parámetros) y devolver un resultado.

```python
def nombre_funcion(params):
    # cuerpo de la función
    return valor
```

En Python las funciones son **first-class objects**, lo que significa que puedes tratarlas como cualquier otro valor:

```python
# Asignar a una variable
mi_func = saludar

# Pasar como argumento a otra función
ejecutar(mi_func)

# Retornar desde otra función
return mi_func
```

---

## Parámetro vs Argumento

Son conceptos distintos que se confunden mucho:

**Parámetro** → la variable que defines en la firma de la función. Está vacía, esperando un valor.  
**Argumento** → el valor real que pasas cuando llamas la función.

```python
# a y b son PARÁMETROS
def sumar(a, b):
    return a + b

# 3 y 5 son ARGUMENTOS
sumar(3, 5)
```

---

## 1. Positional Arguments

Son argumentos asignados **por posición**. Python los empareja en orden: el primero va al primer parámetro, el segundo al segundo, y así sucesivamente.

```python
def crear_usuario(nombre, edad, ciudad):
    print(nombre, edad, ciudad)

crear_usuario("Ana", 25, "Lima")
# nombre="Ana", edad=25, ciudad="Lima"
```

### El orden importa — y Python no te avisa si te equivocas

```python
# ✅ Correcto
crear_usuario("Ana", 25, "Lima")
# nombre="Ana", edad=25, ciudad="Lima"

# ❌ Incorrecto — Python no lanza error, pero los datos están mal
crear_usuario(25, "Ana", "Lima")
# nombre=25, edad="Ana", ciudad="Lima"
```

Python asigna por posición sin validar tipos ni significado. El bug puede ser silencioso y difícil de encontrar.

---

## 2. Keyword Arguments

Son argumentos que pasas usando el nombre del parámetro explícitamente. El orden ya no importa porque Python sabe a qué parámetro pertenece cada valor.

```python
crear_usuario(nombre="Ana", edad=25, ciudad="Lima")

# Mismo resultado aunque cambies el orden
crear_usuario(ciudad="Lima", nombre="Ana", edad=25)
```

### Por qué son más legibles

```python
# ❌ Con positional — ¿qué significa True? ¿y 30?
crear_cuenta("Juan", "juan@gmail.com", 30, "Peru", True)

# ✅ Con keyword — se lee solo
crear_cuenta(
    nombre="Juan",
    email="juan@gmail.com",
    edad=30,
    pais="Peru",
    activo=True
)
```

### Combinando positional y keyword

Puedes mezclarlos, pero **los positional siempre van primero**:

```python
# ✅ Correcto: primero positional, luego keyword
enviar_email("cliente@gmail.com", "Factura", urgente=True)

# ❌ Error de sintaxis: keyword antes que positional
enviar_email(destinatario="cliente@gmail.com", "Factura")
```

---

## 3. Default Values

Un valor por defecto es un **valor de respaldo** asignado a un parámetro. Si no se pasa argumento al llamar la función, Python usa ese valor automáticamente.

```python
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ana")              # Hola Ana  ← usa el default
saludar("Ana", "Buenas")    # Buenas Ana ← sobrescribe el default
```

### Parámetros obligatorios vs opcionales

```python
def crear_usuario(nombre, activo=True):
    print(nombre, activo)

# nombre es obligatorio, activo es opcional
crear_usuario("Juan")         # Juan True
crear_usuario("Juan", False)  # Juan False
```

> **Regla:** los parámetros con default van siempre **después** de los obligatorios. Ponerlos antes es un error de sintaxis.

```python
# ✅ Correcto
def conectar(host, puerto=5432):
    pass

# ❌ SyntaxError
def conectar(puerto=5432, host):
    pass
```

---

## Resumen

| Tipo | Sintaxis | ¿Cuándo usarlo? |
|---|---|---|
| Positional | `f(1, 2)` | Pocos parámetros, orden claro |
| Keyword | `f(a=1, b=2)` | Muchos parámetros, más legibilidad |
| Default value | `def f(a, b=10)` | Parámetros opcionales con valor por defecto |

---
---

# Funciones: `*args`, `**kwargs` y `return` — Episodio 10

## 1. `*args` — Argumentos posicionales variables

`*args` permite que una función acepte **cualquier cantidad de argumentos posicionales**. Python los empaqueta automáticamente en una **tupla**.

Lo importante es el asterisco `*`, no el nombre `args` (puedes llamarlo como quieras).

```python
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

sumar(3, 5)           # 8
sumar(3, 5, 7, 10)    # 25
sumar()               # 0  ← también funciona con cero argumentos
```

Cuando llamas `sumar(3, 5, 7, 10)`, Python hace esto internamente:

```python
args = (3, 5, 7, 10)   # es una tupla
```

### Combinando con parámetros normales

```python
def saludar(saludo, *nombres):
    for nombre in nombres:
        print(f"{saludo}, {nombre}")

saludar("Hola", "Ana", "Luis", "Pedro")
# Hola, Ana
# Hola, Luis
# Hola, Pedro
```

`saludo` recibe el primer argumento posicional, y `*nombres` captura **todo lo que quede**.

> `*args` siempre va después de los parámetros normales.

---

## 2. `**kwargs` — Argumentos con nombre variables

`**kwargs` permite que una función acepte **cualquier cantidad de argumentos con nombre** (`clave=valor`). Python los empaqueta en un **diccionario**.

```python
def mostrar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar(nombre="Ana", edad=25, ciudad="Lima")
# nombre: Ana
# edad: 25
# ciudad: Lima
```

Internamente Python crea:

```python
kwargs = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}
```

### Diferencia entre `*args` y `**kwargs`

| | `*args` | `**kwargs` |
|---|---|---|
| Tipo de argumento | Posicional | Con nombre (`clave=valor`) |
| Tipo resultante | `tuple` | `dict` |
| Ejemplo de llamada | `f(1, 2, 3)` | `f(nombre="Ana")` |

### Orden correcto cuando se combinan

```python
# Obligatorio seguir este orden:
def ejemplo(a, *args, **kwargs):
    print(a)       # int
    print(args)    # tupla
    print(kwargs)  # dict

ejemplo(1, 2, 3, x=10, y=20)
# a     → 1
# args  → (2, 3)
# kwargs → {'x': 10, 'y': 20}
```

El orden es siempre: **parámetros normales → `*args` → `**kwargs`**.

### Caso real: Django ORM

Django usa `**kwargs` internamente en su ORM. Cuando escribes:

```python
User.objects.filter(nombre="Ana", edad=25)
```

`filter` recibe `kwargs = {"nombre": "Ana", "edad": 25}` y construye la consulta SQL a partir de ese diccionario.

---

## 3. `return` — Devolver valores

`return` devuelve un valor desde la función al punto donde fue llamada. **Cuando se ejecuta, la función termina inmediatamente.**

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)   # 8
```

### Puedes devolver cualquier objeto

```python
def obtener_numeros():
    return [1, 2, 3, 4]          # lista

def obtener_usuario():
    return {"nombre": "Ana"}     # diccionario

def coordenadas():
    return (10, 20)              # tupla
```

### "Múltiples valores" es en realidad una tupla

Cuando haces `return a, b, c`, Python en realidad devuelve **una sola tupla**. La coma es lo que crea la tupla, no los paréntesis.

```python
def datos_usuario():
    return "Ana", 25, "Lima"   # Python interpreta: return ("Ana", 25, "Lima")

# Desempaquetado
nombre, edad, ciudad = datos_usuario()
print(nombre)   # Ana
print(edad)     # 25
```

### Sin `return` → la función devuelve `None`

```python
def saludar(nombre):
    print(f"Hola {nombre}")
    # no hay return

resultado = saludar("Ana")   # imprime "Hola Ana"
print(resultado)              # None
```

### Early return — salida anticipada

Puedes usar `return` para salir antes de que la función termine. Evita `if` anidados y hace el código más limpio.

```python
def dividir(a, b):
    if b == 0:
        return None       # ← sale aquí, no llega al return de abajo
    return a / b

print(dividir(10, 0))    # None
print(dividir(10, 2))    # 5.0
```

---

## Resumen

| Concepto | Tipo resultante | ¿Cuándo usarlo? |
|---|---|---|
| `*args` | `tuple` | Cantidad variable de argumentos posicionales |
| `**kwargs` | `dict` | Cantidad variable de argumentos con nombre |
| `return` | cualquier objeto | Devolver el resultado al llamador |

```python
# Todo junto
def ejemplo(a, *args, **kwargs):
    return a, args, kwargs
```

---
---

# Importaciones en Python — Episodio 14

## ¿Qué es un módulo?

Un módulo es simplemente un archivo `.py` con código reutilizable: funciones, clases, variables. Su propósito es organizar el código en partes manejables y evitar conflictos entre nombres.

```python
# matematicas.py
def sumar(a, b):
    return a + b

PI = 3.14159
```

---

## Tipos de módulos

**Propios** — archivos `.py` que escribes tú para tu proyecto.

**Biblioteca estándar** — vienen con Python, no requieren instalación: `os`, `math`, `datetime`, `pathlib`, etc.

**Externos** — instalados con `pip` desde PyPI: `requests`, `numpy`, `pandas`, etc.

```bash
pip install requests
```

```python
import requests
r = requests.get("https://api.ejemplo.com")
```

---

## Formas de importar

### `import modulo` — importa el módulo completo

```python
import math
import os

resultado = math.sqrt(25)   # accedes con prefijo
ruta = os.getcwd()
```

Ventaja: siempre sabes de dónde viene cada función. Desventaja: tienes que escribir el prefijo cada vez.

### `from modulo import nombre` — importa elementos específicos

```python
from math import sqrt, pi
from os import getcwd, listdir

resultado = sqrt(25)        # sin prefijo
archivos = listdir(".")
```

Ventaja: código más conciso. Desventaja: puede ser confuso el origen si hay muchos imports.

### `import modulo as alias` — importa con alias

Muy útil para módulos con nombres largos o cuando la comunidad tiene una convención establecida:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array = np.array([1, 2, 3])
df = pd.DataFrame(data)
```

### `from modulo import nombre as alias`

```python
from math import sqrt as raiz
resultado = raiz(25)
```

### Import condicional — para dependencias opcionales

```python
try:
    import ujson as json    # más rápido si está instalado
except ImportError:
    import json             # fallback a la biblioteca estándar
```

### Import dentro de una función — carga diferida

Útil cuando el módulo es muy pesado y no siempre se necesita:

```python
def procesar_imagen(ruta):
    from PIL import Image   # solo se importa cuando se llama esta función
    img = Image.open(ruta)
    return img
```

---

## La mala práctica: `from modulo import *`

**Nunca hagas esto.** Importa todo el contenido del módulo sin que sepas qué entró.

```python
from os.path import *
from math import *

# ¿De dónde viene 'join'? ¿De os.path o de otra cosa?
resultado = join("a", "b")   # misterio total
```

Tiene tres problemas graves:

**Contaminación del namespace** — introduce cientos de nombres en tu espacio local sin que lo sepas.

**Sobreescritura silenciosa** — si dos módulos definen `calcular()`, el segundo pisa al primero sin ningún error ni aviso.

**Imposible rastrear el origen** — leer el código se vuelve una pesadilla de mantenimiento.

---

## Paquetes y `__init__.py`

Un paquete es una **carpeta** que contiene módulos. Para que Python la reconozca como paquete, necesita un archivo `__init__.py`.

```
mi_proyecto/
├── main.py
└── calculadora/
    ├── __init__.py     ← hace que esta carpeta sea un paquete
    ├── suma.py
    ├── resta.py
    └── division.py
```

### Sin `__init__.py` → error

```python
import calculadora
# ModuleNotFoundError: No module named 'calculadora'
```

### Con `__init__.py` → funciona

```python
import calculadora
from calculadora import suma

resultado = suma.sumar(3, 4)   # 7
```

### Qué puedes hacer en `__init__.py`

**Puede estar vacío** — su sola presencia convierte la carpeta en paquete.

**Imports de conveniencia** — expones lo más importante en la raíz del paquete para simplificar el uso:

```python
# calculadora/__init__.py
from .suma import sumar
from .resta import restar

# Ahora el usuario puede hacer directamente:
from calculadora import sumar   # en vez de: from calculadora.suma import sumar
```

**Controlar `__all__`** — define qué se exporta si alguien usa `import *`:

```python
# calculadora/__init__.py
__all__ = ["sumar", "restar"]
```

**Código de inicialización** — se ejecuta una sola vez, la primera vez que se importa el paquete:

```python
# calculadora/__init__.py
VERSION = "1.0.0"
print(f"Calculadora v{VERSION} cargada")
```

> En Python 3.3+ existen los *namespace packages* (carpetas sin `__init__.py`), pero son un caso especial. En proyectos reales, **siempre incluye el `__init__.py`**.

---

## Imports absolutos vs relativos

Dado este proyecto:

```
mi_paquete/
├── __init__.py
├── modulo_a.py
└── subpaquete/
    └── modulo_b.py
```

### Absoluto — desde la raíz del proyecto

```python
# dentro de subpaquete/modulo_b.py
import mi_paquete.modulo_a
from mi_paquete import modulo_a
```

Siempre claro y explícito. Recomendado por PEP 8. Funciona desde cualquier contexto.

### Relativo — con puntos como referencia

```python
# dentro de subpaquete/modulo_b.py
from .. import modulo_a           # .. = directorio padre
from ..modulo_a import mi_func
```

`.` = directorio actual, `..` = directorio padre. Solo funciona dentro de un paquete, no en scripts ejecutados directamente.

**Usa absolutos siempre que puedas.** Los relativos solo tienen sentido dentro de paquetes que se moverán como unidad.

---

## Orden correcto de imports — PEP 8

Agrupa los imports en tres bloques separados por una línea en blanco:

```python
# 1. Biblioteca estándar
import os
import sys
from pathlib import Path

# 2. Librerías de terceros (pip)
import numpy as np
import requests

# 3. Módulos propios del proyecto
from mi_paquete import utilidades
from mi_paquete.modelos import Usuario
```

---

## Errores comunes

**`ModuleNotFoundError`** — el módulo no está instalado o hay un typo:

```python
import numpay   # typo
# ModuleNotFoundError
```

Solución: `pip install numpy` y verificar el nombre exacto en PyPI.

**`ImportError`** — el módulo existe pero la función que intentas importar no:

```python
from math import square_root   # no existe
# ImportError: cannot import name 'square_root'
```

Solución: usa `dir(math)` para ver qué contiene el módulo.

**Circular import** — el módulo A importa B y B importa A. Python entra en un bucle:

```python
# a.py
from b import func_b

# b.py
from a import func_a   # ¡bucle infinito!
```

Solución: mover el import dentro de la función que lo necesita, o rediseñar la arquitectura para eliminar la dependencia circular.

---

## Convenciones de nombres — PEP 8

| Elemento | Convención | Correcto | Incorrecto |
|---|---|---|---|
| Clases | `PascalCase` | `class MiCalculadora` | `class mi_calculadora` |
| Archivos / Módulos | `snake_case` | `mi_modulo.py` | `MiModulo.py` |
| Funciones | `snake_case` | `def calcular_area()` | `def CalcularArea()` |
| Variables | `snake_case` | `nombre_usuario` | `NombreUsuario` |
| Constantes | `UPPER_SNAKE_CASE` | `MAX_INTENTOS = 3` | `maxIntentos = 3` |
| Atributos privados | `_snake_case` | `_datos_internos` | `datosInternos` |
| Métodos mágicos | `__dunder__` | `__init__`, `__str__` | `Init`, `Str` |