
# poly --> many
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('animals making sound')
    

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('bark bark')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Bleeh')


kitte = Cat('Kittey')
kitte.make_sound()

shepherd = Dog('Mike')
shepherd.make_sound()

goat1 = Goat('Khashi-1')
goat1.make_sound()
goat2 = Goat('Khashi-2')


animals = [kitte, shepherd, goat1, goat2]
for animal in animals:
    animal.make_sound()