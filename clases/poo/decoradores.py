class Perfil:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, nueva_password):
        if len(nueva_password) < 6:
            raise ValueError("❌ La contraseña debe tener al menos 6 caracteres.")
        self.__password = nueva_password

usuario = Perfil("admin125")

print(usuario.password)

usuario.password = "nuevaClave99"
print(usuario.password)