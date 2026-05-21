from datetime import datetime

class User:
    
    def __init__(self, name, age):
        self.today = datetime.now()
        self.name = name
        self.age = age

    def calculate_birth_year(self, already_had_birthday: bool) -> str:
        """Calcular el año de nacimiento"""
        current_year = self.today.year
        birth_year = (current_year - self.age) if already_had_birthday else (current_year - self.age - 1)
        return f"Hola {self.name}, tu año de nacimineto es {birth_year}"