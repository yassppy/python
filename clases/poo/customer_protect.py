class Customer:
    def __init__(self, name, age, saldo):
        self.name = name
        self.age = age
        self._saldo = saldo #protegido
    
customer = Customer("Juan", 30, 1500)

## Python no prohibe el acceso y la modificación solo es una convención entre programadores
print(f"Se puede acceder a su valor: {customer._saldo}")