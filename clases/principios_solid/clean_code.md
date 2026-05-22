# Clean Code y Refactorización en Python

El objetivo de Clean Code es escribir código que sea:

- Fácil de leer
- Fácil de entender
- Fácil de mantener
- Fácil de reutilizar

La idea principal es:

> "El código se escribe una vez, pero se lee muchas veces."

La refactorización consiste en mejorar la estructura interna del código sin cambiar su comportamiento.

Es decir:

Antes:

- Funciona ✔
- Difícil de entender ❌

Después:

- Funciona igual ✔
- Más limpio ✔
- Más reutilizable ✔

---

# Reglas principales de Clean Code

# 1. Nombres descriptivos

El nombre debe explicar qué hace algo sin necesidad de comentarios.

## Incorrecto

```python
x = 150
d = 0.18

r = x*d
```

Nadie sabe qué representan esas variables.

---

## Correcto

```python
precio_producto = 150
impuesto = 0.18

monto_impuesto = precio_producto * impuesto
```

Ahora se entiende inmediatamente.

---

# Regla:

Si tienes que explicar el nombre, probablemente está mal nombrado.

---

# 2. Funciones pequeñas

Una función debería hacer una sola cosa.

---

## Incorrecto

```python
def procesar_usuario():

    validar_usuario()

    guardar_usuario()

    enviar_correo()

    generar_reporte()

    actualizar_estadisticas()
```

Hace demasiadas cosas.

---

## Correcto

```python
def validar_usuario():
    print("Validando")


def guardar_usuario():
    print("Guardando")


def enviar_correo():
    print("Enviando correo")
```

Uso:

```python
validar_usuario()
guardar_usuario()
enviar_correo()
```

Cada función tiene una responsabilidad.

---

# Regla:

Funciones pequeñas = menos errores.

---

# 3. Evitar números mágicos

Los números escritos directamente generan confusión.

---

## Incorrecto

```python
precio_final = precio * 1.18
```

¿Qué significa 1.18?

---

## Correcto

```python
IGV = 0.18

precio_final = precio*(1+IGV)
```

Ahora es claro.

---

# Regla:

Usar constantes para valores importantes.

---

# 4. Evitar código duplicado

Duplicar código produce problemas:

- Más mantenimiento
- Más errores
- Más trabajo

---

## Incorrecto

```python
precio1 = 100
igv1 = precio1*0.18

precio2 = 200
igv2 = precio2*0.18
```

La lógica se repite.

---

## Correcto

```python
def calcular_igv(precio):
    return precio*0.18


producto1 = calcular_igv(100)
producto2 = calcular_igv(200)
```

La lógica ahora es reutilizable.

---

# Principio DRY

DRY significa:

Don't Repeat Yourself

"No te repitas"

---

# 5. Evitar comentarios innecesarios

El código debería explicarse por sí mismo.

---

## Incorrecto

```python
# Multiplica el precio por el impuesto

resultado = precio*impuesto
```

El comentario es redundante.

---

## Correcto

```python
monto_impuesto = precio*impuesto
```

El nombre ya explica qué ocurre.

---

# Cuándo usar comentarios

Usar comentarios para:

✔ explicar reglas de negocio  
✔ explicar algoritmos complejos  
✔ advertencias importantes

No para explicar cosas obvias.

---

# Refactorización

La refactorización consiste en mejorar código existente sin modificar su resultado.

---

# Caso real

Supongamos un sistema de tienda.

Código inicial:

```python
def calcular_total():

    precio1 = 100
    precio2 = 50
    precio3 = 20

    total = precio1+precio2+precio3

    impuesto = total*0.18

    total_final = total+impuesto

    return total_final
```

Funciona, pero tiene problemas:

- Datos escritos manualmente
- Poco reutilizable
- Difícil de mantener

---

# Refactorizado

```python
IGV = 0.18


def calcular_total(productos):

    subtotal = sum(productos)

    impuesto = subtotal*IGV

    return subtotal+impuesto
```

Uso:

```python
productos=[100,50,20]

resultado=calcular_total(productos)

print(resultado)
```

Ventajas:

✔ reutilizable  
✔ menos código  
✔ más claro  
✔ más mantenible

---

# Técnicas comunes de refactorización

# Extraer método

Separar bloques grandes en funciones pequeñas.

---

## Antes

```python
def pedido():

    print("Validando usuario")

    print("Calculando total")

    print("Enviando correo")
```

---

## Después

```python
def validar_usuario():
    print("Validando usuario")


def calcular_total():
    print("Calculando total")


def enviar_correo():
    print("Enviando correo")


def pedido():

    validar_usuario()

    calcular_total()

    enviar_correo()
```

---

# Reemplazar condicionales grandes

---

## Antes

```python
def descuento(tipo):

    if tipo=="gold":
        return 0.20

    elif tipo=="silver":
        return 0.10

    elif tipo=="bronze":
        return 0.05
```

---

## Después

```python
descuentos={

    "gold":0.20,
    "silver":0.10,
    "bronze":0.05
}


def descuento(tipo):

    return descuentos.get(tipo,0)
```

Más limpio y fácil de extender.

---

# Reutilización de código en Python

La reutilización consiste en escribir una vez y usar muchas veces.

Formas comunes:

1. Funciones

```python
def saludar(nombre):

    return f"Hola {nombre}"
```

---

2. Clases

```python
class Calculadora:

    def sumar(self,a,b):
        return a+b
```

---

3. Herencia

```python
class Animal:

    def respirar(self):
        print("Respirando")


class Perro(Animal):
    pass
```

---

4. Composición

Más recomendada que herencia en muchos casos.

```python
class Motor:

    def encender(self):
        print("Motor encendido")


class Auto:

    def __init__(self):

        self.motor=Motor()
```

Auto usa Motor sin heredar.

---

# Frase rápida para recordar

Clean Code:

"Escribir código para humanos"

Refactorización:

"Mejorar sin cambiar resultados"

Reutilización:

"Escribir una vez y usar muchas veces"
