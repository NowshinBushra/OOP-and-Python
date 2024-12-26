
# encapsulation : hide details (basically use hoy implemented detail gulo hide korte)
# access modifier : Private, Public, Protected

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name      # "public"
        self.__balance = initial_deposit   # evabe 2ta '__' diye dile "Private" hoy, class er baire theke access (change) kora jay na (error dekhabe). class er moddhe use kora jabe
        self._branch = 'banani'            #eta 1ta '_' diye "Protected" bujhay, just a convention, baire theke access kora jay

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nai'


    
rafsan = Bank('choto vai', 10000)

# print(rafsan.__balance)   # AttributeError: 'Bank' object has no attribute '__balance'
rafsan.deposit(40000)
print(rafsan.get_balance())

print(rafsan.holder_name)
rafsan.holder_name = 'boro vai'
print(rafsan.holder_name)


"""
# forcefully private jinish gulo dekhte hole:
print(dir(rafsan)) # <-- this will give an output, from that output find your desired attribute(private)
print(rafsan._Bank__balance)

"""
