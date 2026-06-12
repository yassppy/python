# Patrones de diseño
## Principios SOLID

- **Single Responsibility (SRP)**: Una clase debe tener una única razón para cambiar,
  es decir, una sola responsabilidad.

- **Open/Closed (OCP)**: Una clase debe estar abierta para extenderse
  pero cerrada para modificarse.

- **Principio de sustitución de Liskov (LSP)**: Cualquier objeto de la clase padre
  puede ser reemplazado por el objeto de la clase hija sin alterar el comportamiento
  del programa.

- **Interface Segregation (ISP)**: Una clase no debe verse obligada a implementar
  métodos de una interfaz que no necesita. Es mejor tener interfaces pequeñas
  y específicas que una grande y general.

- **Dependency Inversion (DIP)**: Las clases de alto nivel no deben depender de
  clases de bajo nivel. Ambas deben depender de abstracciones (interfaces o clases abstractas). De esa forma puedes cambiar las implementaciones concretas sin romper el resto del programa.

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

## Patrón de diseño
Son soluciones generales y reutilizables a problemas comunes en el diseño de software.
Es como un plano que puedes adaptar a tu proyecto para simplificar la complejidad.

> ⚠️ En proyectos simples puede ser innecesariamente complejo, por eso se aplica
> principalmente en proyectos complejos.

---

### Patrones creacionales
Resuelven CÓMO se crean los objetos, incrementando la flexibilidad y reutilización.

- **PATRÓN SINGLETON**: Solo existe una única instancia de la clase en todo el programa.
  > Como el presidente de un país, solo puede haber uno a la vez.

- **PATRÓN FACTORY METHOD**: Una clase decide qué objeto crear según el contexto,
  sin que el código sepa exactamente cuál es.
  > Como una fábrica que produce distintos productos según el pedido.

- **PATRÓN ABSTRACT FACTORY**: Crea familias de objetos relacionados sin especificar
  sus clases concretas.
  > Como una fábrica de muebles que produce silla, mesa y sofá del mismo estilo.

- **PATRÓN BUILDER**: Construye objetos complejos paso a paso.
  > Como armar una hamburguesa: pan, carne, queso, lechuga, uno por uno.

- **PATRÓN PROTOTYPE**: Crea nuevos objetos copiando uno existente.
  > Como hacer fotocopias de un documento original.

---

### Patrones estructurales
Resuelven CÓMO se componen los objetos para formar estructuras más grandes.

- **PATRÓN DECORATOR**: Agrega funcionalidades a un objeto sin modificar su clase.
  > Como agregar toppings a un helado, el helado base no cambia.

- **PATRÓN COMPOSITE**: Agrupa objetos en estructuras de árbol para tratarlos
  como si fueran uno solo.
  > Como una carpeta que contiene archivos y otras carpetas.

- **PATRÓN PROXY**: Un objeto actúa como intermediario para controlar el acceso
  a otro objeto.
  > Como un guardia de seguridad que decide quién puede entrar.

---

### Patrones de comportamiento
Resuelven CÓMO interactúan y se comunican los objetos entre sí.

- **PATRÓN STRATEGY**: Define una familia de algoritmos en clases separadas
  y los hace intercambiables. Puedes cambiar el objeto referenciado y su
  comportamiento en tiempo de ejecución sin modificar el contexto.
  > Como enchufar distintos comportamientos a una clase,
  > si quieres otro comportamiento, simplemente cambias el enchufe.
