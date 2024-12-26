# read only --> you can not set or change the value
# getter --> get a value of a property through a method. Most of the time you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time you will set the value of a private property.

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    def age1(self):
        return self._age
    
    #getter       (getter without any setter is readonly attribute)
    @property  # this is a "Decorator"
    def age2(self):  # here age is no more a method, decorator converts it as an attribute
        return self._age
    
    #getter
    @property  
    def salary(self):
        return self.__money

    #setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value
    
    
    
sam = User('kopa', 21, 12000)

print(sam.age1())   # this will give output - 21
# print(sam.age2())   # this will give "TypeError: 'int' object is not callable"
print(sam.age2)  # as age2() is now an attribute (this will give output - 21)

print(sam.salary)   # this will give output - 12000
sam.salary = 4500  # this will give an error without setter (AttributeError: property 'salary' of 'User' object has no setter)
print(sam.salary)   # this will give output - 16500