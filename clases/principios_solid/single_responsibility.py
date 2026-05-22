# Sistema de gestión para una biblioteca
#
# Requisitos:
# 1. Registrar libros
# 2. Procesar préstamos
#
# Instrucción:
# Refactorizar usando SRP: Una clase debe tener una unica responsabilidad, es decir que su métodos debe 
# estar alineado a eso tambien. 

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f'Libro: {self.title}, Autor: {self.author}, Copias: {self.copies}'

class User:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    
    def __str__(self):
        return f"Usuario: {self.name}, Número: {self.number}, Email: {self.email}"

class BookRegister:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print("Registro exitoso")

class LoanProcessor:
    def borrow_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            print(f'{user.name} tiene el libro {book.title} prestado quedan {book.copies} copias')
        else:
            print(f'No hay libros disponibles')
            


book_python = Book("Python Crash Course, 3rd Edition", "Eric Matthes", 100)
user = User("Juan", "963678345", "mg@gmail.com")
user_miguel = User("miguel", "963678345", "mg@gmail.com")
book_register = BookRegister()
print(book_python)
print(user)
book_register.add_book(book_python)
print(book_register.books[0])
loan = LoanProcessor()
loan.borrow_book(user=user, book=book_python)
loan.borrow_book(user=user_miguel, book=book_python)