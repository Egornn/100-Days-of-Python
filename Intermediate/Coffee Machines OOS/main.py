from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()
while True:
    order = input(f'What would you like {coffee_menu.get_items()}? ')
    drink: MenuItem = coffee_menu.find_drink(order)
    if drink is None:
        if order == "off":
            exit()
        if order == "report":
            coffee_machine.report()
        continue
    else:
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)



