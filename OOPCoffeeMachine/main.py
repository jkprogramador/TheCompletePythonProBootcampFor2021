from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        if "off" == choice:
            break
        elif "report" == choice:
            coffee_machine.report()
            money_machine.report()
        else:
            menu_drink = menu.find_drink(choice)

            if coffee_machine.is_resource_sufficient(menu_drink):

                if money_machine.make_payment(menu_drink.cost):
                    coffee_machine.make_coffee(menu_drink)


main()
