class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial 

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("❌ Error: El saldo no puede ser negativo.")
        else:
            self.__saldo = nuevo_saldo

cuenta = CuentaBancaria("Miguel", 1000)
print(f"Saldo actual: ${cuenta.get_saldo()}")

cuenta.set_saldo(1500)
print(f"Nuevo saldo: ${cuenta.get_saldo()}")