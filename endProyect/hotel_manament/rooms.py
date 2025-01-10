
class Rooms:
    def __init__(self, room_number: int, room_type: str, room_price: int, room_status: bool):
        self.room_number = room_number
        self.room_type = room_type
        self.room_price = room_price
        self.room_status = room_status | True

    def __str__(self):
        return f"Room number: {self.room_number}, Room type: {self.room_type}, Room price: {self.room_price}, Room status: {self.room_status} "
    
class RoomManagement:
    rooms = []
    def __init__(self):
        self.rooms = []
    
    def addRoom(self, room: Rooms):
        self.rooms.append(room)
    
    def showRooms(self):
        for room in self.rooms:
            print(room)
    
    def check_availability(self, room_number: int):
        for room in self.rooms:
            if room.room_status == True and room.room_number == room_number:
                return print(f'Room {room_number} esta disponible')
        return print(f'Room {room_number} no esta disponible')
    
    @classmethod
    def deleteRoom(cls, room_number: int):
        for room in cls.rooms:
            if room.room_number == room_number:
                cls.rooms.remove(room)
                return True
        return False