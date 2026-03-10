import requests

response = requests.get("https://fakestoreapi.com/products")
products = response.json() # Retorna una lista

for product in products:
    name = product["title"]
    price = product["price"]
    print(f'{name} cuesta {price}')