<p align="center">
  <img src="assets/banner.png" alt="Base de Datos Banner" width="100%">
</p>

# Curso de Python

Bienvenido en esta parte encontraras recursos para aprender Python.

---

## 📚 Contenido

### Clases
- **Clase 01** — Concepto de Variable y Nomenclatura
- **Clase 02** — Tipos de Datos
- **Clase 03** — Módulo Matemático
- **Clase 04** — Expresiones Regulares

### Proyectos
- **automatizar_facturas** — Extracción automática de facturas con expresiones 
regulares para una empresa que vende accesorios de motocicletas. El registro 
manual tomaba 10 o más minutos y se redujo a menos de 5 minutos.
  
## ⚙️ Configuración del entorno virtual

```bash
# 1. Crear el entorno virtual
uv venv

# 2. Activar el entorno (Windows)
.venv\Scripts\activate

# 3. Inicializar el proyecto (crea el pyproject.toml)
uv init

# 4. Instalar dependencias
uv add pdfplumber

uv add pandas openpyxl

# 5. Ejecutar
cd proyectos/facturas

uv run extraer_facturas.py

# 6. Desactivar el entorno
deactivate
```

## 📚 Recuros

- Versiones de Python se utilizara la versión 3.12.10 https://www.python.org/downloads/windows/

- Gestor de depencias para Python para proyectos modernos: https://docs.astral.sh/uv/#highlights

- Extensiones en Visual Studio Code: 
  - https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat
  - https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
  - https://marketplace.visualstudio.com/items?itemName=enkia.tokyo-night

- Para practicar algoritmos de datos:
  - https://www.alg0.dev/