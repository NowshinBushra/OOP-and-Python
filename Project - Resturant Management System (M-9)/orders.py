class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity   # jodi cart e item ta already thake
        else:
            self.items[item] = item.quantity    # jodi cart e item ta na thake


    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items = {}