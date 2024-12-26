class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)


class AcBus(Bus):
    def __init__(self, name, price, seat) -> None:
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'Seat: {self.seat}')
        return super().__repr__()

class PickUpVan(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


green_line = AcBus('Green-Line', 500000, 30)
print(green_line)