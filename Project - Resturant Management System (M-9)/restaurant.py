
from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []  # eta hocche amader employees er database
        self.menu = Menu()  # ekhane menu hocche ekhon FoodItem class er instance

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print('Employee List!!!')
        for emp in self.employees:
            print(emp.name, emp.email, emp.address, emp.salary)