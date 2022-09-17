class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity



    def rent_dvd(self, customer_id, dvd_id):

        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        age = customer.age
        name = customer.name
        restriction = dvd.age_restriction

        if dvd in customer.rented_dvds:
            return f"{name} has already rented {dvd.name}"

        if dvd.is_rented:
            return f"DVD is already rented"

        if age < restriction:
            return f"{name} should be at least {restriction} to rent this movie"

        return f"{name} has successfully rented {dvd.name}"



    def return_dvd(self, customer_id, dvd_id):

        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"



        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"

        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"

        return result.strip()
