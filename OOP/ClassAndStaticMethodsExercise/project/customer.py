class Customer:
    id = 1
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        result = Customer.id
        Customer.id += 1
        return result

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# cus1 = Customer("name", "add", "email")
# print(cus1.id)
# cus2 = Customer("name1", "add2", "mail2")
# print(cus2.id)