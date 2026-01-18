class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):

        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"HOUSE at {self.address}\n"
            f"Area: {self.area}m2, Rooms: {self.rooms}, Plot: {self.plot}m2\n"
            f"Price: ${self.price}"
        )


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"FLAT at {self.address}\n"
            f"Area: {self.area}m2, Rooms: {self.rooms}, Floor: {self.floor}\n"
            f"Price: ${self.price}"
        )


my_house = House(150.0, 5, 500000, "Willow Creek 12", 1000)
my_flat = Flat(60.0, 3, 250000, "Market Square 5/12", 4)

print(my_house)
print("-" * 20)
print(my_flat)
