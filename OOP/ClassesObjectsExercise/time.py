class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours < 10:
            hours = "0" + str(self.hours)
        else:
            hours = str(self.hours)

        if self.minutes < 10:
            minutes = "0" + str(self.minutes)
        else:
            minutes = str(self.minutes)

        if self.seconds < 10:
            seconds = "0" + str(self.seconds)
        else:
            seconds = str(self.seconds)


        return f"{hours}:{minutes}:{seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())