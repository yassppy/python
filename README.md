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
- **Clase 05** — Estructuras de control

### Proyectos
- **automatizar_facturas** — Extracción automática de facturas con expresiones 
regulares para una empresa que vende accesorios de motocicletas. El registro 
manual tomaba 10 o más minutos y se redujo a menos de 5 minutos.
- **Consumimos una API** - Consumo de API y se aplica lo aprendido del ciclo for.
  
## ⚙️ Configuración del entorno virtual


### 1. Clonar un repositorio solamente la última versión
```bash
git clone https://github.com/yassppy/python.git --depth=1
```
### 2. Crear el entorno virtual (instalar uv antes de ejecutar)
```bash
uv venv
```
### 3. Activar el entorno (Windows)
```bash
.venv\Scripts\activate
```
### 4. Inicializar el proyecto (crea el pyproject.toml)
```bash
uv init
```
### 5. Instalar dependencias
```bash
uv add pdfplumber
```
```bash
uv add pandas openpyxl
```
```bash
uv add requests
```
### 6. Ejecutar
```bash
cd proyectos/facturas
```
```bash
uv run extraer_facturas.py
```
### 7. Desactivar el entorno (Cuando termines)
```bash
deactivate
```

## 📚 Recuros

- Libro que se va a utilizar: https://www.amazon.com/Python-Crash-Course-Eric-Matthes/dp/1718502702

- Versiones de Python se utilizara la versión más estable 3.13.12: https://www.python.org/downloads/windows/

- Para ver las versiones estables ingresar aquí: https://docs.python.org/3/

- Gestor de depencias para Python para proyectos modernos: https://docs.astral.sh/uv/#highlights

- Extensiones en Visual Studio Code: 
  - https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat
  - https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
  - https://marketplace.visualstudio.com/items?itemName=enkia.tokyo-night

- Para practicar algoritmos de datos:
  - https://www.alg0.dev/

- Api que se utiliza para el ejercicio: https://fakestoreapi.com/docs#tag/Products/operation/getAllProducts