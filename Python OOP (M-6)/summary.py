class Book:
    def __init__(self, name) -> None:
        self.name = name

    def read1(self):
        pass         #pass dile ignore kore chole jay, error dey na
    def read2(self):
        raise NotImplementedError  # this will force the subclass to be implemented

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)

    def read2(self):
        print('reading physics vector')

topon = Physics('Topon', True)
print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read1()
topon.read2()


"""
             |---inheritance
    OOP------|---encapsulation
             |---abstract
             |---polymorphism

"""