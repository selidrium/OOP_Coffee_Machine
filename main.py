from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order? {options}").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
        else:
            print("Replenish resources... Turning off")
            is_on = False


print("Come again soon")