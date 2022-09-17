import datetime

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        year = int(date.split(".")[2])
        month = date.split(".")[1]
        datetime_object = datetime.datetime.strptime(month, "%m")
        full_month_name = datetime_object.strftime("%B")
        return cls(name, id, year, full_month_name, age_restriction)

    def __repr__(self):
        rented = ""
        if self.is_rented:
            rented = "rented"
        else:
            rented = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"