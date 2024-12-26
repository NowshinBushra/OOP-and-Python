
# abc = abstract base class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod   #enforce all derived class to have a eat method
    def eat(self):
        print('')

    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()

    def eat(self):
        print('eating banana')


monkey = Monkey('lucky')
monkey.eat()


###  Abstract class VS Interface