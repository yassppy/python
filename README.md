<p align="center">
  <img src="assets/banner.png" alt="Base de Datos Banner" width="100%">
</p>

# 🐍 Curso de Python

Bienvenido. En esta sección encontrarás todos los recursos necesarios para aprender Python.

---

## 📑 Tabla de Contenido

- [Clases](#-clases)
- [Proyectos](#-proyectos)
- [Configuración del Entorno Virtual](#️-configuración-del-entorno-virtual)
- [Recursos](#-recursos)

---

## 🎓 Clases

| # | Tema |
|---|------|
| Clase 01 | Concepto de Variable y Nomenclatura |
| Clase 02 | Tipos de Datos |
| Clase 03 | Módulo Matemático |
| Clase 04 | Expresiones Regulares |
| Clase 05 | Estructuras de Control |
| Clase 06 | Programación Orientada a Objetos |
| Clase 07 | Algoritmos y Complejidad Algorítmica |
| Clase 08 | Patrones de Diseño y Principios SOLID |

---

## 🚀 Proyectos

### `automatizar_facturas`
Extracción automática de facturas con expresiones regulares para una empresa que vende accesorios de motocicletas. El registro manual tomaba 10 o más minutos y se redujo a menos de 5 minutos.

### `consumimos_una_api`
Consumo de una API aplicando lo aprendido del ciclo `for`.

### `app_gestion_de_tareas`
Aplicación para gestión de tareas.

---

## ⚙️ Configuración del Entorno Virtual

### 1. Clonar el repositorio (solo la última versión)
```bash
git clone https://github.com/yassppy/python.git --depth=1
```

### 2. Crear el entorno virtual
> Requiere tener `uv` instalado previamente.
```bash
uv venv
```

### 3. Activar el entorno (Windows)
```bash
.venv\Scripts\activate
```

### 4. Inicializar el proyecto
> Esto crea el archivo `pyproject.toml`.
```bash
uv init
```

### 5. Instalar dependencias
```bash
uv add pdfplumber
uv add pandas openpyxl
uv add requests
```

### 6. Ejecutar el proyecto
```bash
cd proyectos/facturas
uv run extraer_facturas.py
```

### 7. Desactivar el entorno
```bash
deactivate
```

---

## 📚 Recursos

### 📖 Libros y Documentación

| Recurso | Enlace |
|---------|--------|
| Python Crash Course (libro del curso) | [Amazon](https://www.amazon.com/Python-Crash-Course-Eric-Matthes/dp/1718502702) |
| Descargar Python 3.13 (Windows) | [python.org](https://www.python.org/downloads/windows/) |
| Versiones estables de Python | [docs.python.org](https://docs.python.org/3/) |
| Gestor de dependencias `uv` | [astral.sh/uv](https://docs.astral.sh/uv/#highlights) |
| Generación de PDFs con fpdf2 | [py-pdf.github.io](https://py-pdf.github.io/fpdf2/) |
| Análisis de datos con Pandas | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| Patrones de diseño | [refactoring.guru](https://refactoring.guru/es/design-patterns) |

---

### 🛠️ Extensiones para Visual Studio Code

| Extensión | Enlace |
|-----------|--------|
| GitHub Copilot Chat | [Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) |
| Python | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python) |
| Pylance | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) |
| Tokyo Night (tema) | [Marketplace](https://marketplace.visualstudio.com/items?itemName=enkia.tokyo-night) |

---

### 🧮 Práctica de Algoritmos

| Recurso | Enlace |
|---------|--------|
| alg0.dev | [alg0.dev](https://www.alg0.dev/) |
| Big-O Calculator (PyPI) | [pypi.org](https://pypi.org/project/big-O-calculator/) |

---

### 🖥️ Interfaces Gráficas con Flet

| Recurso | Enlace |
|---------|--------|
| Documentación oficial | [flet.dev/docs](https://flet.dev/docs) |
| Ejemplos en GitHub | [github.com/MagnoEfren/flet](https://github.com/MagnoEfren/flet) |
| Flet Playground | [fletplaygraund.pages.dev](https://fletplaygraund.pages.dev/) |

---

### 🤖 Bot de Telegram

Para uno de los proyectos necesitarás una cuenta de Telegram y un bot configurado. Sigue estos pasos:

1. Descarga la app [1.1.1.1](https://play.google.com/store/search?q=1.1.1.1&c=apps) y actívala para poder acceder a Telegram.
2. Abre Telegram, acepta los términos y crea tu cuenta.
3. Una vez creada la cuenta, puedes desactivar la app anterior.
4. En el buscador de Telegram escribe `@BotFather` (con verificación) y selecciónalo.
5. Presiona **Start** y usa el comando `/newbot` para crear tu bot siguiendo las instrucciones.

**Referencias:**
- [Documentación de bots de Telegram](https://core.telegram.org/bots/samples)
- [pyTelegramBotAPI en GitHub](https://github.com/eternnoir/pyTelegramBotAPI)

---

### 🌐 API de Práctica

- [Fake Store API — Productos](https://fakestoreapi.com/docs#tag/Products/operation/getAllProducts)

---

### 💡 Práctica de Lógica de Programación

| Recurso | Enlace |
|---------|--------|
| LeetCode Patterns | [seanprashad.com](https://seanprashad.com/leetcode-patterns/) |
| LeetCode | [leetcode.com](https://leetcode.com/) |
| Consoly (app móvil) | [Google Play](https://play.google.com/store/apps/details?id=app.consoly) |
