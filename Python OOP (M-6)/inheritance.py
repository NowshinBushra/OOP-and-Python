

# base class, parent class, common attribute + functionality class
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'running laptop: {self.brand}'


# derived class, child class, uncommon attribute + functionality class
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim

        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'sending message to: {number} with text: {text}'
        
    def __repr__(self) -> str:
        return f'Phone: {self.brand}, {self.price}, {self.dual_sim}'


class Laptop(Gadget):
    def __init__(self, memory) -> None:
        
        self.memory = memory

class Camera:
    def __init__(self, lens) -> None:
        self.lens = lens



# inheritance
my_phone = Phone('iPhone', 120000, 'black', 'Canada', 'dual-sim')
print(my_phone.brand)
print(my_phone)
# my_phone.phone_call()