
#from reservations import add_reservation

class Customers():
    def __init__(self, name: str, email: str, phone: int):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

class CustomerManagement:
    customers = []
    def __init__(self):
        self.customers = []
    
    def addCustomer(self, customer: Customers):
        self.customers.append(customer)
    
    def showCustomers(self):
        for customer in self.customers:
            print(customer.showCustomer())
    
    def deleteCustomer(self, name: str):
        for customer in self.customers:
            if customer.name == name:
                self.customers.remove(customer)
                return True
        return False