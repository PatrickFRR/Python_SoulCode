from email.headerregistry import Address


class Client:
    def __init__(self, name):
        self.__name = name
        self.__address = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def enter_address(self, city):
        self.__address.append(Address(city))

    def list_address(self):
        for address in self.__address:
            print(address.city)

class Address:
    def __init__(self, city):
        self.__city = city

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

client1 = Client('John')
client1.enter_address('Florida')
print(client1.name)
# John
client1.list_address()
# Florida
del client1