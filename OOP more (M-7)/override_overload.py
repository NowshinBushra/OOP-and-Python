class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

#   override
    def eat(self):
        print('evergy drinks')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # override
    def eat(self):
        print('vegetables')
        
    def exercise(self):
        print('go to gym')

#   + sign overload
    def __add__(self, other):
        return self.age + other.age
    
#   * sign overload
    def __mul__(self, other):
        return self.weight * other.weight   # python dunder methods
    
#   len overload
    def __len__(self):
        return self.weight
    
#   > operator overload
    def __gt__(self, other):
        return self.age > other.age
        

sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 35, 68, 91, 'BD')

# sakib.eat()
# sakib.exercise()


# plus sign overload
print(45 + 49)
print('sakib' + 'Mushfiq')
print([1,2] + [3,4,5])

# ---------add, mul, len, greaterThan----------------
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)