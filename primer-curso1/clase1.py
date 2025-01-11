jugador1 = "papel"
jugador2 = "piedra"

if jugador1 == "papel" and jugador2 == "tiguera" or jugador1 == "roca" and jugador2 == "papel" or jugador1 == "tigeras" and jugador2 == "roca" :
    print("jugador 2 haga con ", jugador2)
elif jugador1 == "papel" and jugador2 == "piedra" or jugador1 == "roca" and jugador2 == "tigera" or jugador1 == "tigeras" and jugador2 == "papel" :
    print("jugador 1 haga con ", jugador1)
else:
    print("jugaron la misma mano")


def sumatoria (n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n - 1)

print(sumatoria(5))


def funcion_a(x):
    if x == 0:
        return x
    return x + funcion_b(x - 1)

def funcion_b(x):
    if x == 0:
        return x
    return x + funcion_a(x - 1)

print(funcion_a(5))

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")
            else:
                print(f"te sales de tu tarifa actual que es de {self.balance}")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

#Llamada a los metodos
account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)