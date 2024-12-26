# Customer
# Employee
# Admin
from orders import Order
from abc import ABC

class Users(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Employee(Users):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee('sam', 'sam@gmail.com', 1234566, 'dhaka',32, 'chef', 12000)
# print(emp.name)


class Customer(Users):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()    # ekhane cart ta hocche ekhon Order() class er instance, so amra ekhn self.cart ke use kore Order class er joto variable, functions ache sob access kore use korte parbo


    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('Item added')
        else:
            print("item not found")

    def view_cart(self):
        print("**view cart**")
        print("Name\tprice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()





class Admin(Users):
    def __init__(self, name, email, phone, address,):
        super().__init__(name, email, phone, address)

    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_menu_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()





# adm = Admin('John', 'john@gmail', 3764287, 'dhaka')
# # adm.add_employee('sam', 'sam@gmail.com', 1234566, 'dhaka', 32, 'chef', 12000)

# item =FoodItem('Pizza', 12, 10)
# item2 =FoodItem('Burger', 10, 30)
# ph_restaurent = Restaurant("*********Phitron********")

# adm.add_new_item(ph_restaurent, item)
# adm.add_new_item(ph_restaurent, item2)

# mn = Menu()
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# mn.show_menu()

# customer1 = Customer("Joe", "joe@gmail", 2546432, "Vienna")
# customer1.view_menu(ph_restaurent)
# # adm.view_employee()

# itemName = input("Enter item name: ")
# item_quantity = int(input("Enter item quantity: "))

# customer1.add_to_cart(ph_restaurent, itemName, item_quantity)
# customer1.view_cart()