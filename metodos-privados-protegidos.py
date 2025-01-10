
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self.__registros_transacciones = []

    def __registrar_transaccion(self, cantidad):
        self.__registros_transacciones.append(cantidad)
        print(f"Transacción registrada: {self.__registros_transacciones}")
    
    def _actualizar_saldo(self, cantidad):
        self._balance += cantidad
        print(f"su saldo anterios era de {self._balance - cantidad} ahora su saldo es de {self._balance}")
        self.__registrar_transaccion(cantidad)

    def show_balance(self):
        print(f"El saldo de {self.name} es de {self._balance} con la cantidad de movimientos '{self.__registros_transacciones} '")
        

user1 = Bank('Carlos', 1000)
user1._actualizar_saldo(500)
user1.show_balance()
print("---------------------------")
user1._actualizar_saldo(900)
user1.show_balance()