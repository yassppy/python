# Habit Tracker

## Descomponer el problema

### Como se va ver la interfaz del usuario?
  - Va a ser ingresada solamente por números desde el 0 al 6. Si ingresa un número o letra fuera de este rango, se le pedirá que ingrese un número válido.
  - Se debe pedir el nombre del usuario en cada primera interacción. 
  0. Salir
  1. Agregar un nuevo hábito
  2. Marcar un hábito como completado
  3. Ver hábitos del día (cuales hizo y cual falta)
  4. Ver streaks (cuántos días seguidos ha completado el hábito) de cada hábito.
  5. Listar todos los hábitos con detalle.
  6. Eliminar un hábito.

### Qué voy a guardar en el habitó creado? 
  - Nombre
  - Descripción
  - Fecha de creación se crea automáticamente al momento de crear el hábito.
  - Lista de checks vacia al momento de crear el hábito.
  - Historial de dias en que el usuario ha completado el hábito.

### Restricicones:
  - El nombre y la descripción deben ser nomalizados en este caso va ser todo minúsculas para eso se utilizara ``.lower()``
  - No se puede realizar el check de un hábito que no existe.
