# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
    cart = []
    origin = 'China'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna city'   # instance attribute
        self.location = 'jam er majh khane'

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and remaining {remaining} ')

    @classmethod
    def hudai_dekhi(self, item):
        print('just ac er hawa khaite aschi', item)

    @staticmethod  # used to do some utility task (+/-/*...)
    def multiply(a,b): # static method, self parameter dite hobe na. so Instance chara use korte parbo
        result= a*b
        print(result)


# Shopping.purchase(2, 3, 4) # 1 missing argument (self soho chay)
Shopping.purchase('a', 2, 3, 4)

bashundahra =  Shopping('basu and dhara', 'location not popular')
bashundahra.hudai_dekhi('lungi') 
Shopping.hudai_dekhi('Lungi')  # done by classmethod (self pass kora lageni)

Shopping.multiply(4,5) # static method
