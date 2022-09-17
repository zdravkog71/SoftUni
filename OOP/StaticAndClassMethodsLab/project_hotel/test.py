from StaticAndClassMethodsLab.project_hotel.hotel import Hotel
from StaticAndClassMethodsLab.project_hotel.room import Room

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
print(hotel.guests)

hotel.take_room(1, 2)
print(hotel.guests)
print("Room guests")
print(first_room.guests)
hotel.free_room(1)
print(hotel.guests)
print(first_room.is_taken)
#hotel.take_room(3, 1)
#hotel.take_room(3, 1)

print(hotel.status())

