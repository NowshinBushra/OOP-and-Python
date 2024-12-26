from food_item import FoodItem
from menu import Menu
from users import Users, Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order


restaurant_name = Restaurant("Amar Restaurant")


def customer_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(restaurant_name)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(restaurant_name, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name} !!")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View item")
        print("5. Delete item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(restaurant_name, item)

        elif choice == 2:
            name = input("Employee name: ")
            email = input("Employee email :")
            phone = input("Employee phone: ")
            address = input("Employee address: ")
            age = input("Employee age: ")
            designation = input("Employee designation: ")
            salary = input("Employee salary: ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(restaurant_name, employee)

        elif choice == 3:
            admin.view_employee(restaurant_name)
            
        elif choice == 4:
            admin.view_menu(restaurant_name)

        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(restaurant_name, item_name)

        elif choice == 6:
            break
        else:
            print("Invalid input") 


while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input!!")