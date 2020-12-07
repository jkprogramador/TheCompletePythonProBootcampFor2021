MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def prompt() -> str:
    """
    Prompts the user for an action.
    """
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def print_report(balance: float):
    """
    Prints each resource item available and the current amount of money in the machine.
    """
    for item, value in resources.items():
        item = item.capitalize()

        if "Coffee" == item:
            print(f"{item}: {value}g")
        else:
            print(f"{item}: {value}ml")

    print(f"Balance: ${balance:.2f}")


def check_availability(coffee_type: str) -> dict:
    """
    Checks if the machine has all available resources.
    Returns a dictionary {"available": bool, "error": str} denoting if
    all resources are available and, in case they are not, what kind of
    error message should be displayed.
    """
    ingredients = MENU[coffee_type]["ingredients"]
    result = {"available": True, "error": ""}

    for ingredient, amount in ingredients.items():
        if amount > resources[ingredient]:
            result["available"] = False
            result["error"] = f"Sorry there is not enough {ingredient}."
            break

    return result


def prompt_for_coins() -> dict:
    """
    Prompts the user for inserting coins.
    Returns a dictionary with a key/value pair representing the type of coin/amount.
    Ex.: {"quarters": 1, "dimes": 0, "nickles": 0, "pennies": 0}.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return {
        "quarters": quarters,
        "dimes": dimes,
        "nickles": nickles,
        "pennies": pennies
    }


def process_coins(coins: dict) -> float:
    """
    Calculates each coin value in the given coins dictionary.
    Returns the total amount for the given coins.
    """
    conversion = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    total = 0.0

    for coin, amount in coins.items():
        total += conversion[coin] * amount

    return total


def check_transaction(balance: float, money_amount: float, coffee_type: str) -> dict:
    """
    Processes the user's order by checking the amount of money against the price
    of the chosen coffee type.
    Returns a dictionary {"ok": bool, "error": str, "change_amount": float, balance: float} denoting
    if the transaction is ok, the amount of change that should be returned
    to the user and the current total balance.
    In case the transaction is not ok, the dictionary will have an error message.
    """
    coffee_price = MENU[coffee_type]["cost"]
    result = {
        "ok": True,
        "error": "",
        "change_amount": 0.0,
        "balance": balance
    }

    if coffee_price > money_amount:
        result["ok"] = False
        result["error"] = "Sorry that's not enough money. Money refunded."
    else:
        result["balance"] = balance + coffee_price

        if money_amount > coffee_price:
            result["change_amount"] = round(money_amount - coffee_price, 2)

    return result


def make_coffee(coffee_type: str):
    """
    Makes coffee, deducting the resources needed by the coffee type from the coffee machine.
    """
    ingredients = MENU[coffee_type]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["milk"] -= ingredients.get("milk", 0)
    resources["coffee"] -= ingredients.get("coffee", 0)

    print(f"Here is you {coffee_type}. Enjoy!")


def main():
    balance = 0

    """
    Main loop of the program.
    """
    while True:
        # TODO: 1. Prompt the user by asking "What would you like? (espresso/latte/cappuccino):"
        choice = prompt()

        # TODO: 2. Turn off the Coffee Machine by entering "off" in the prompt.
        if "off" == choice:
            break
        elif "report" == choice:
            # TODO: 3. Print report.
            print_report(balance)
        elif choice in MENU:
            # TODO: 4. Check if the machine's resources are sufficient.
            resource_status = check_availability(choice)

            if not resource_status["available"]:
                print(resource_status["error"])
            else:
                # TODO: 5. Process coins.
                coins = prompt_for_coins()
                money_amount = process_coins(coins)

                # TODO: 6. Check if the transaction is successful.
                transaction = check_transaction(balance, money_amount, choice)

                if not transaction["ok"]:
                    print(transaction["error"])
                else:
                    balance = transaction["balance"]

                    if transaction["change_amount"] > 0:
                        print(f"Here is ${transaction['change_amount']:.2f} dollars in change.")

                    # TODO: 7. Make coffee.
                    make_coffee(choice)


main()
