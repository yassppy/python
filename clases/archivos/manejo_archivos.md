# Archivos, Excepciones y JSON en Python

---

## 📁 Archivos

### Lectura y Escritura con `open()`

La función incorporada `open()` permite acceder a archivos. Los modos principales son:

- `'r'` — leer
- `'w'` — escribir (sobreescribe)
- `'a'` — añadir al final
- `'b'` — modo binario

Siempre se recomienda usar el **gestor de contexto `with`**, que cierra el archivo automáticamente incluso si ocurre un error, previniendo fugas de recursos.

```python
# Escritura
with open('saludo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('Hola, Mundo!\n')

# Lectura
try:
    with open('saludo.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no fue encontrado.")
```

---

### Lectura Eficiente

| Método | Descripción | Recomendación |
|--------|-------------|---------------|
| `.read()` | Lee todo el archivo como `str` | ⚠️ Solo para archivos pequeños |
| `.readlines()` | Lee todas las líneas como `list` | ⚠️ Solo para archivos pequeños |
| Iteración `for linea in f` | Procesa línea por línea (streaming) | ✅ Recomendado para archivos grandes |

```python
# Streaming — mínimo uso de memoria
with open('large_log.txt', 'r', encoding='utf-8') as f:
    for linea in f:
        print(linea.strip())
```

---

### `pathlib` — Rutas Orientadas a Objetos

Introducido en Python 3.4, `pathlib.Path` ofrece una API orientada a objetos para trabajar con rutas de forma multiplataforma.

```python
from pathlib import Path

ruta = Path('datos') / 'mi_archivo.txt'           # operador / para construir rutas
ruta.parent.mkdir(parents=True, exist_ok=True)    # crear directorio si no existe

ruta.write_text('Contenido.', encoding='utf-8')   # escribir
contenido = ruta.read_text(encoding='utf-8')      # leer

if ruta.exists():
    print(f"Archivo: {ruta.name}")
```

Métodos útiles: `.exists()`, `.is_file()`, `.name`, `.parent`, `.mkdir()`, `.open()`.

---

## ⚠️ Excepciones

### ¿Qué es una excepción?

Un error detectado durante la ejecución que interrumpe el flujo normal del programa. El bloque `try-except` permite capturarlo y evitar terminaciones abruptas.

### Excepciones comunes

| Excepción | Causa |
|-----------|-------|
| `FileNotFoundError` | Archivo no encontrado |
| `PermissionError` | Sin permisos de acceso |
| `TypeError` | Tipo de dato incorrecto |
| `ValueError` | Valor inesperado |
| `KeyError` | Clave no existe en un `dict` |
| `ZeroDivisionError` | División por cero |

```python
try:
    resultado = 10 / 0
    with open('datos.txt', 'r') as f:
        contenido = f.read()
except ZeroDivisionError:
    print("Error: división por cero")
except FileNotFoundError:
    print("Error: archivo no encontrado")
except (TypeError, ValueError) as e:
    print(f"Error de tipo/valor: {e}")
```

---

### Estructura completa: `try · except · else · finally`

| Bloque | Cuándo se ejecuta |
|--------|-------------------|
| `try` | Código propenso a errores |
| `except` | Si ocurre una excepción coincidente |
| `else` | Solo si `try` finaliza **sin** errores |
| `finally` | **Siempre** — para limpieza de recursos |

```python
def dividir_y_escribir(a, b, path):
    try:
        resultado = a / b
        f = open(path, 'w')
        f.write(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
    except TypeError:
        print("Error: operandos deben ser numéricos")
    else:
        print("Guardado con éxito")
    finally:
        if 'f' in locals() and not f.closed:
            f.close()
```

---

## `{}` JSON

### ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de texto ligero, legible por humanos y máquinas, estándar para APIs web y archivos de configuración.

### Equivalencias Python ↔ JSON

| Python | JSON |
|--------|------|
| `dict` | `object {}` |
| `list` / `tuple` | `array []` |
| `str` | `string ""` |
| `int` / `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

### Módulo `json` — 4 funciones clave

| Función | Dirección | Descripción |
|---------|-----------|-------------|
| `json.dumps(obj)` | Python → `str` | Serializa objeto a cadena JSON |
| `json.loads(s)` | `str` → Python | Deserializa cadena JSON a objeto |
| `json.dump(obj, fp)` | Python → archivo | Serializa directo a archivo |
| `json.load(fp)` | archivo → Python | Deserializa desde archivo |

---

### Guardar y leer archivos JSON

```python
import json

# Serializar a archivo
usuario = {"id": 101, "nombre": "Ana", "activo": True, "cursos": ["Python", "Bases de Datos"]}

try:
    with open('usuario.json', 'w', encoding='utf-8') as f:
        json.dump(usuario, f, indent=4)
    print("Datos guardados")
except IOError as e:
    print(f"Error: {e}")

# Deserializar desde archivo
try:
    with open('usuario.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
    print(f"Nombre: {datos['nombre']}")
except FileNotFoundError:
    print("Archivo no encontrado")
except json.JSONDecodeError as e:
    print(f"JSON inválido: {e}")
```

---

### JSON en memoria — `dumps` y `loads`

```python
import json

usuario = {"id": 101, "nombre": "Ana", "activo": True}

# Serializar a cadena
json_string = json.dumps(usuario, indent=4, sort_keys=True)
# indent=4     → salida con sangría legible
# sort_keys=True → claves ordenadas alfabéticamente

# Deserializar desde cadena
datos = json.loads(json_string)
print(datos['nombre'])  # Ana
```

> `json.loads()` lanza `json.JSONDecodeError` si la cadena no es JSON válido. Siempre usar con `try-except`.

---

### Limitaciones de JSON y serialización personalizada

El módulo `json` estándar **no puede serializar tipos complejos** como `datetime`, `set`, clases personalizadas o `bytes`.

| Tipo problemático | Solución |
|-------------------|----------|
| `datetime` | `.isoformat()` → `str` ISO 8601 |
| `set` | `list(s)` → convertir a lista |
| clase personalizada | `.__dict__` → convertir a `dict` |
| `bytes` | `.decode()` → convertir a `str` |

La solución recomendada es pasar una función al parámetro `default=` de `json.dumps()`:

```python
import json
from datetime import datetime

def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"{obj.__class__.__name__} no es serializable")

evento = {"nombre": "Lanzamiento", "fecha": datetime.now()}

resultado = json.dumps(evento, indent=4, default=custom_serializer)
# "fecha": "2026-04-27T10:30:00"
```

---

## Buenas Prácticas — Resumen

- Usar siempre `with` al abrir archivos para garantizar el cierre.
- Preferir **iteración línea a línea** sobre `.read()` para archivos grandes.
- Usar `pathlib.Path` en lugar de concatenar strings para construir rutas.
- Capturar **excepciones específicas**, nunca usar `except:` sin tipo.
- Envolver siempre `json.loads()` y `json.load()` en `try-except JSONDecodeError`.
- Usar `default=` en `json.dumps()` para tipos no serializables por defecto.
