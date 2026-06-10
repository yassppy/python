# Patrones de diseño
## Principios SOLID

- **Single Responsibility (SRP)**: Una clase debe tener una única razón para cambiar,
  es decir, una sola responsabilidad. **/semana01/factura.py**

- **Open/Closed (OCP)**: Una clase debe estar abierta para extenderse
  pero cerrada para modificarse. **/semana01/descuento.py**

- **Principio de sustitución de Liskov (LSP)**: Cualquier objeto de la clase padre
  puede ser reemplazado por el objeto de la clase hija sin alterar el comportamiento
  del programa. Se encuentra en los ejercicios de la **/semana02**

- **Interface Segregation (ISP)**: Una clase no debe verse obligada a implementar
  métodos de una interfaz que no necesita. Es mejor tener interfaces pequeñas
  y específicas que una grande y general.**/semana03/gestor_archivos_isp.py**

- **Dependency Inversion (DIP)**: Las clases de alto nivel no deben depender de
  clases de bajo nivel. Ambas deben depender de abstracciones (interfaces o clases abstractas). De esa forma puedes cambiar las implementaciones concretas sin romper el resto del programa.**/semana03/gestor_archivos_dip.py**

### Frase para memorizar SOLID

S → Una clase, una sola responsabilidad.
O → Abierta para extender, cerrada para modificar.
L → La clase padre puede ser reemplazado por las clases hijas sin alterar el comportamiento del programa.
I → Interfaces pequeñas y específicas, no una gigante.
D → Depende de abstracciones, no de implementaciones concretas.

## Clean Code:

Escribir código fácil de leer, entender, mantener y reutilizar para humanos.
-  **Nombres descriptivos**: Los nombres de las variables, funciones y clases deben ser descriptivos y autoexplicativos. Como ``precio_producto`` y no ``x``.
- **Funciones pequeñas**: Una función debe hacer una sola cosa. Por ejemplo:
```python
def enviar_correo():
    print("Enviando correo")

def procesar_pedido():
    validar_usuario()
    calcular_total()
    enviar_correo()
```
- **Evitar números mágicos**: Usar constantes para valores importantes. En vez de `precio * 1.18` usar `IGV = 0.18`
- **Evitar código duplicado (DRY)**: Don't Repeat Yourself.
 Si la misma lógica aparece dos veces, conviértela en una función reutilizable.
- **Evitar comentarios innecesarios**: El código debe explicarse por sí mismo.
  Usar comentarios solo para reglas de negocio, algoritmos complejos o advertencias importantes.

### Frases para recordar
- Clean Code → *"Escribir código para humanos"*
- Refactorización → *"Mejorar sin cambiar resultados"*
- Reutilización → *"Escribir una vez y usar muchas veces"*
