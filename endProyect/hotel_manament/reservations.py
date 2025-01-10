
from .rooms import Rooms, RoomManagement
from .payment import proccesPayment
from .customers import Customers

class Reservation (Rooms):

    def __init__(self, room_number: int, room_type: str, room_price: int, days: int):
        self.room_number = room_number
        self.room_type = room_type
        self.room_price = room_price
        self.days = days

    def __str__(self):
        return f"numero de habitacion: {self.room_number}, tipo de habitacion: {self.room_type}, dias: {self.days} con el valor de: {self.room_price}" 
        
class ReservationManagement (RoomManagement):
    
    def __init__(self):
        self.reservations = []
    
    async def addReservation(self, customers: Customers, reservation: Reservation, rooms: Rooms):
        conditions = [
            (rooms.room_price != reservation.room_price, "El monto no coincide con el precio de la habitacion"),
            (rooms.room_status == False, f"La habitacion no esta disponible, losiento {customers.name} busca otra habitacion"),
            (reservation.days < 1, "La cantidad de dias no es valida"),
            (rooms.room_number != reservation.room_number, "El numero de habitacion no coincide")
        ]

        for condition, message in conditions:
            if condition:
                print(message)
                return
            
        payment_result = await proccesPayment(customers.name, rooms.room_price)
        print(payment_result)

        rooms.room_status = False
        self.reservations.append(reservation)
        print(f"### el usario {customers.name} ha reservado la habitacion {reservation.room_number} por {reservation.days} dias")
        
    
    def showReservations(self):
        for reservation in self.reservations:
            print(reservation)
    
    def deleteReservation(self, room_number: int):
        for reservation in self.reservations:
            if reservation.room_number == room_number:
                self.reservations.remove(reservation)
                return True
        return False