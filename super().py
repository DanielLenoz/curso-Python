class Vehicle:
    def __init__(self, brand, model, price): #los atributos de la calse padre
        self.brand = brand
        self.model = model
        self.price = price

class Car(Vehicle):#tenermos que mencionar la heredad para el "super()" para que tenga un señalador interno
		#los atributos de la case padre tambien tiene que ser mencionandos en el constructor junto al atributo exclusiva
    def __init__(self, brand, model, price, number_of_doors):
        # Llama al constructor de la clase padre (Vehicle)
        super().__init__(brand, model, price)
        # Agrega un atributo exclusivo para la clase Car
        self.number_of_doors = number_of_doors

# Crear una instancia de Car
car1 = Car("Toyota", "Corolla", 20000, 4)
print(car1.brand)  # "Toyota" (heredado de Vehicle)
print(car1.number_of_doors)  # 4 (atributo exclusivo de Car)