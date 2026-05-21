# 🏷️ Guía de Nomenclatura en Python (Normas PEP 8)

En Python, la forma en que escribes el nombre de una carpeta, un archivo o una clase le dice al mundo exactamente qué tipo de elemento es antes de leer una sola línea de código. Seguir estas reglas (basadas en la guía oficial de estilo **PEP 8**) separa a un programador novato de uno profesional.

Recuerden que es buena practica poner todo en inglés.

---

## 📁 1. Carpetas (Paquetes) 👉 *Todo en minúsculas y nombres cortos*

Cuando creas carpetas para organizar los módulos de tus proyectos, la regla es mantener la máxima simplicidad posible para evitar fallos de compatibilidad entre sistemas operativos.

* **Formato:** Todo en minúsculas y preferiblemente de una sola palabra.
* **¿Y si son dos palabras?** Intenta evitarlo, pero si es estrictamente necesario por claridad, únelas con un guion bajo (`_`).
* ❌ **Mal:** `/Mis-Clases/`, `/Modelos_De_Gatos/`, `/Controladores Del Sistema/` *(¡Nunca uses espacios ni guiones medios!)*.
* ✅ **Bien:** `/modelos/`, `/vistas/`, `/utils/`, `/gestion_usuarios/`.

---

## 📄 2. Archivos (Módulos) 👉 *Estilo snake_case*

Los nombres de tus archivos con extensión `.py` deben seguir rigurosamente el formato **snake_case** (el caso de la serpiente 🐍).

* **Formato:** Todo en minúsculas. Si el nombre se compone de dos o más palabras, deben separarse obligatoriamente con un **guion bajo (`_`)**.
* ❌ **Mal:** `GatoSimpsons.py`, `nuevo-carro.py`, `Main_File.py`.
* ✅ **Bien:** `gato.py`, `auto_electrico.py`, `main.py`, `conexion_base_datos.py`.

---

## 🏛️ 3. Clases 👉 *Estilo PascalCase (o CapWords)*

Las clases representan los moldes estructurales o los conceptos lógicos más importantes de tu software. Para que resalten instantáneamente sobre todo lo demás, se usa **PascalCase** y en **Singular**.

* **Formato:** Cada palabra que compone el nombre debe iniciar con **Mayúscula**, y van todas completamente pegadas (sin espacios ni guiones bajos).
* ❌ **Mal:** `class autoelectrico:`, `class Perro_Cazador:`, `class Animales`.
* ✅ **Bien:** `class GatoSimpson:`, `class AutoElectrico:`, `class CuentaBancaria:`.

---

## 🛠️ 4. Variables, Atributos y Métodos 👉 *Estilo snake_case*

Todo lo que viva en el interior de tu código (las variables, las funciones globales, los métodos de un objeto y sus atributos asociados) comparte exactamente la misma regla física que los nombres de archivos.

* **Formato:** Letras minúsculas separadas por guiones bajos (`_`) para simular espacios.
* ❌ **Mal:** `def ArrancarMotor():`, `self.ColorOjos = "Verde"`, `miCarro = Carro()`.
* ✅ **Bien:** `def arrancar_motor(self):`, `self.color_ojos = "Verde"`, `mi_carro = Carro()`.

---

## 🎯 Tabla Resumen de Nomenclaturas

Usa esta tabla como mapa de referencia rápido para estructurar tus entornos de desarrollo:

| Elemento Estructural | Estilo Visual | Ejemplo Real en Código |
| :--- | :--- | :--- |
| **Carpeta (Paquete)** | Corto, minúsculas | `/controladores/` o `/utils/` |
| **Archivo (Módulo)** | `snake_case` | `cuenta_ahorros.py` |
| **Clase (El Molde)** | `PascalCase` | `class CuentaAhorros:` |
| **Método (La Acción)** | `snake_case` | `def depositar_dinero(self):` |
| **Atributo (El Dato)** | `snake_case` | `self.saldo_disponible = 1000` |
| **Variable Común** | `snake_case` | `total_a_pagar = 150.50` |