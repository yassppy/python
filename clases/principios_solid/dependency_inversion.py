from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self):
        pass


class MySQLDatabase(Database):
    def save(self):
        print("Guardando en MySQL")


class PostgreSQLDatabase(Database):
    def save(self):
        print("Guardando en PostgreSQL")

class LoanProcessor:
    def __init__(self, database):
        self.database = database

    def process(self):
        self.database.save()

db = MySQLDatabase()
loan = LoanProcessor(db)
loan.process()