class Car:
    """
    Representa vehiculos del mundo real
    """
    total_wheels = 4

    def __init__(self, make, color):
        self.make = make
        self.color = color
    
    def star(self):
        print(f'El carro {self.make} arranco')


car_tesla = Car("tesla", "negro")

print(f'El carro 1 es un {car_tesla.make} de color {car_tesla.color}')
print(f'El número de ruedas es {car_tesla.total_wheels}')
car_tesla.star()