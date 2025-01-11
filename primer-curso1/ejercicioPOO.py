from typing import Any

class Carros:
    def __init__(self, modelo, color, matricula):
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.disponible = True

    def rentado(self):
        if self.disponible:
            self.disponible = False
            print(f"el carro de modelo {self.modelo} esta dispoblie")
        else:
            print(f"el carro de modelo {self.modelo} no esta dispoblie")

    def devolver_carro(self):
        self.disponible = True
        print(f"el carro de modelo {self.modelo} fue devuelto")
        

class Usuario:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.carro_rentado = []
    
    def rentar_carro(self, carro):
        if carro.disponible:
            carro.rentado()
            self.carro_rentado.append(carro)
            print(f"el carro que rentaste fue {carro.modelo}")
        else:
            print(f"el carro no esta disponible")

    def devolver_carros(self, carro):
        if carro in self.carro_rentado:
            carro.devolver_carro()
            self.carro_rentado.remove(carro)
            print(f"el carro que rentaste fue {carro.modelo} ya fue devuelto")
        else:
            print(f"no tienes el carro en el garaje")

class Concesionaria:
    def __init__(self):
        self.carros = []
        self.usuarios = []

    def agregar_carro(self, carro):
        self.carros.append(carro)
        print(f"se agrego el carro {carro.modelo}")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"se agrego el usuario {usuario.name}")

    def mostrar_carros_disponibles(self):
        print("Carros disponibles:")
        for carro in self.carros:
            if carro.disponible:
                print(f"- {carro.modelo} de color {carro.color} con matricula {carro.matricula}")  
    def usuarios_registrados(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(f"{usuario.name} con id {usuario.user_id}")          

#crear carros

carro1 = Carros("Toyota", "Rojo", "1234")
carro2 = Carros("Nissan", "Azul", "5678")
carro3 = Carros("Chevrolet", "Blanco", "9101")

#crear usuarios
usuario1 = Usuario("Juan", 1)
usuario2 = Usuario("Pedro", 2)
usuario3 = Usuario("Maria", 3)

#crear concesionaria

concesionaria = Concesionaria()
concesionaria.agregar_carro(carro1)
concesionaria.agregar_carro(carro2)
concesionaria.agregar_carro(carro3)

concesionaria.agregar_usuario(usuario1)
concesionaria.agregar_usuario(usuario2)
concesionaria.agregar_usuario(usuario3)

concesionaria.mostrar_carros_disponibles()
concesionaria.usuarios_registrados()

usuario1.rentar_carro(carro1)
usuario2.rentar_carro(carro2)
usuario3.rentar_carro(carro1)

concesionaria.mostrar_carros_disponibles()

usuario1.devolver_carros(carro1)
usuario2.devolver_carros(carro2)

usuario3.rentar_carro(carro1)

concesionaria.mostrar_carros_disponibles()

