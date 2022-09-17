class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.take_room(people) == None:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room_guests = room.guests
                room.free_room()
                if not room.is_taken:
                    self.guests -= room_guests


    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += "Free rooms: " + ", ".join(free_rooms) + "\n"
        result += "Taken rooms: " + ", ".join(taken_rooms)

        return result



