import asyncio
from hotel_manament.customers import Customers, CustomerManagement
from hotel_manament.reservations import Reservation, ReservationManagement
from hotel_manament.rooms import Rooms,RoomManagement

async def main():

    #usuarios
    user1 = Customers("Juan", "juan@gmail.com" , 123456789)
    user2 = Customers("Pedro", "pedro@gmail.com" , 987654321)
    user3 = Customers("Maria", "maria@gmail.com" , 123456789)
    # print(user1)
    # print(user2)
    #agregar usuarios
    userMgmt = CustomerManagement()
    userMgmt.addCustomer(user1)
    userMgmt.addCustomer(user2)
    userMgmt.addCustomer(user3)

    #crear cuartos
    cuarto1 = Rooms(101, "sencilla", 13000, True)
    cuarto2 = Rooms(102, "doble", 20000, True)
    cuarto3 = Rooms(103, "suite", 30000, True)
    cuarto4 = Rooms(104, "suite", 30000, True)

    #agregar cuartos
    roomMgmt = RoomManagement()
    roomMgmt.addRoom(cuarto1)
    roomMgmt.addRoom(cuarto2)
    roomMgmt.addRoom(cuarto3)
    roomMgmt.addRoom(cuarto4)

    # roomMgmt.check_availability(101)
    #mostrar cuartos
    print("----Cuartos disponibles")
    roomMgmt.showRooms()
    #crear reservaciones
    reservacion1 = Reservation(101, "sencilla", 13000, 2)
    reservacion2 = Reservation(102, "doble", 20000, 3)
    reservacion3 = Reservation(102, "doble", 20000, 3)
    # print(reservacion1)
    # print(reservacion2)

    #agregar reservaciones
    reservacionMgmt = ReservationManagement()

    await reservacionMgmt.addReservation(user1, reservacion1, cuarto1)
    await reservacionMgmt.addReservation(user2, reservacion2, cuarto2)
    await reservacionMgmt.addReservation(user3, reservacion3, cuarto2)

    #mostrar reservaciones
    print("------Reservaciones")
    reservacionMgmt.showReservations()

    print("-----Cuartos disponibles")
    roomMgmt.showRooms()

    # roomMgmt.check_availability(101)

if __name__ == "__main__":
    asyncio.run(main())
