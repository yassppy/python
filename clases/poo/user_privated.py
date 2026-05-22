class User:
    def __init__(self, password):
        self.__password = password
    
user = User("@Juan124@")

## Se puede imprimir
# print(f"acceso publico: {user.__password}")

## Se puede acceder
print(user._User__password)