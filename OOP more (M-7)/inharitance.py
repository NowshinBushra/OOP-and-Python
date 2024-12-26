# inheritance provides you "is_a" relation

class Animal:
    pass

# Dog is_a animal         <---dog e animal er shob property o thakbe + dog er self property o thakbe
class Dog(Animal):
    pass

# Cat is_a animal
class Cat(Animal):
    pass


# -----------


class Furniture:
    pass

# chair is_a furniture         <---chair e furniture er common shob property/method thakbe + chair er extra self property thakbe
class Chair(Furniture):
    pass

# table is_a furniture
class Table(Furniture):
    pass