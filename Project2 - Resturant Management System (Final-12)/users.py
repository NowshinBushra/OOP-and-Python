
from abc import ABC

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.balance = 0
        self.orders = []

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_item_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            self.orders.append((item, quantity))
            print('Item added')
        else:
            print("item not found")


    def view_orders(self):
        print("---view your orders---")
        print("Name\tPrice\tQuantity\tSubtotal")
        for item, quantity in self.orders:
            subtotal = item.price * quantity
            print(f"{item.name}\t${item.price}\t{quantity}\t${subtotal}")
        print(f"Total Price: ${self.total_price}\n")


    def place_order(self):
        Total_price = self.total_price
        if self.balance >= Total_price:
            self.balance -= Total_price
            print(f"Your order is placed.")
            self.orders.clear()
        else:
            print("Insufficient balance. Please add funds.")


    @property
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.orders)


    def available_balance(self):
        print(f"{self.name}, your current balance is: ${self.balance}")
    

    def add_funds(self, amount):
        self.balance += amount
        print(f"{self.name}, ${amount} added to your balance. Current balance: ${self.balance}.")



class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def add_customer(self, restaurant, customer):
        restaurant.add_customer(customer)

    def view_allCustomer(self, restaurant):
        restaurant.view_customers()

    def remove_customer(self, restaurant, customer_email):
        restaurant.remove_customer(customer_email)

    def add_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def update_price(self, restaurant, item_name, item_price):
        restaurant.menu.update_price(item_name, item_price)


class Restaurant():
    def __init__(self, res_name):
        self.res_name = res_name
        self.customers = []
        self.menu = Menu()

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customers(self):
        for customer in self.customers:
            print(f'Customer name: {customer.name}, Email: {customer.email}, Address: {customer.address}')

    def find_customer(self, customer_email):
        for customer in self.customers:
            if customer.email == customer_email:
                return customer
        return None
    
    
    def remove_customer(self, customer_email):
        customer = self.find_customer(customer_email)
        if customer:
            self.customers.remove(customer)
            print("customer deleted")
        else:
            print("customer not found")

            


    def replica():
        pass


class Menu():
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def update_price(self, item_name, item_price):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.price = item_price

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted")
        else:
            print("item not found")

    def show_menu(self):
        print("------Menu------")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity



# from users import User, Customer, Admin, FoodItem, Restaurant, Menu

restaurant_name = Restaurant("Amar Restaurant")


def customer_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    address = input("Enter your Address: ")
    customer = Customer(name=name, email=email, address=address)

    restaurant_name.add_customer(customer)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View your orders")
        print("4. Place your orders")
        print("5. Check available balance")
        print("6. Add Funds to your current balance")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(restaurant_name)

        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_item_to_cart(restaurant_name, item_name, item_quantity)

        elif choice == 3:
            customer.view_orders()
        elif choice == 4:
            customer.place_order()
        elif choice == 5:
            customer.available_balance()
        elif choice == 6:
            amount = int(input("Enter your amount: "))
            customer.add_funds(amount)
        elif choice == 7:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    address = input("Enter your Address: ")
    admin = Admin(name=name, email=email, address=address)

    while True:
        print(f"Welcome {admin.name} !!")
        print("1. Add new item")
        print("2. View menu")
        print("3. Delete item")
        print("4. Update item price")
        print("5. Add new customer")
        print("6. View all customers")
        print("7. Delete customer")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_item(restaurant_name, item)
            
        elif choice == 2:
            admin.view_menu(restaurant_name)

        elif choice == 3:
            item_name = input("Enter item name: ")
            admin.remove_item(restaurant_name, item_name)

        elif choice == 4:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter updated price: "))
            admin.update_price(restaurant_name, item_name, item_price)

        elif choice == 5:
            name = input("Customer name: ")
            email = input("Customer email :")
            address = input("Customer address: ")
            customer = Customer(name, email, address)
            admin.add_customer(restaurant_name, customer)

        elif choice == 6:
            admin.view_allCustomer(restaurant_name)

        elif choice == 7:
            customer_email = input("Enter customer email to remove: ")
            admin.remove_customer(restaurant_name, customer_email)

        elif choice == 8:
            break
        else:
            print("Invalid input") 


while True:
    print("Welcome!!")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input!!")

