class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
customer = Customer("Juan", 30)

## Se puede imprimir
print(f"acceso publico: {customer.name}")

## Se puede modificar
customer.name = "Pedro"
print(f"acceso publico: {customer.name}")
