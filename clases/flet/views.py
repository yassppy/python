import flet as ft
from models import User

class UserView:
    def __init__(self, page: ft.Page):
        self.page = page
        
        # Componentes Visuales para el usuario
        self.name_input = ft.TextField(
            # prefix=ft.Icon(name="person", color=ft.colors.BLUE, size=40),
            prefix_icon=ft.Icon(ft.Icons.SUPERVISED_USER_CIRCLE_OUTLINED, color=ft.Colors.WHITE, size=40),
            label="Ingrese su nombre", 
            width=301,
            border_radius=10,
            filled=True,
        )
        self.age_input = ft.TextField(label="Ingrese su edad", width=300)
        self.birthday_checkbox = ft.Checkbox(
            label="Ya cumplistes en este año?", 
            value=False
        )
        self.result_text = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD)
        self.submit_button = ft.ElevatedButton("Calcular año de nacimiento", on_click=self._handle_submit)
        
        # Construimos la interfaz
        self._build_ui()

    def _build_ui(self):
        """Configura la página y añade los componentes."""
        self.page.title = "Calculadora de año de nacimiento"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        
        # Agregamos todos los nuevos componentes a la pantalla
        self.page.add(
            self.name_input,
            self.age_input,
            self.birthday_checkbox,
            self.submit_button,
            self.result_text
        )

    def _handle_submit(self, e):
        """Manejador del evento del botón (Controlador)."""
        try:
            # 1. Validamos que el nombre no esté vacío
            name = self.name_input.value.strip()
            if not name:
                self.result_text.value = "Ingresar un nombre."
                self.page.update()
                return

            # 2. Capturamos y validamos la edad
            age = int(self.age_input.value)
            if age < 0:
                self.result_text.value = "Edad no puede ser negativo."
                self.page.update()
                return
            
            # 3. Capturamos el valor booleano del Checkbox (True o False)
            already_had_birthday = self.birthday_checkbox.value
            
            # 4. INSTANCIAMOS EL MODELO: Aquí es donde creamos al objeto User con sus datos
            user = User(name=name, age=age)
            
            # 5. Le pedimos al objeto que ejecute su método matemático
            evaluation_result = user.calculate_birth_year(already_had_birthday=already_had_birthday)
            
            # 6. Mostramos el resultado final en la interfaz
            self.result_text.value = evaluation_result
            
        except ValueError:
            self.result_text.value = "Por favor introducir datos validos"
            
        # Refrescamos la pantalla
        self.page.update()