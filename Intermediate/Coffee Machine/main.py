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

VALID_OPTIONS = ["espresso", "latte", "cappuccino", "off", "report"]

COINS = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "pennies": 0.01,
}


def coffe_machine(stock: dict) -> None:

    def print_resources(ingredients: dict, money: float) -> None:
        for key in list(ingredients):
            if key == "water" or key == "milk":
                print(f"{key.capitalize()}: {ingredients[key]}ml" )
            elif key == "coffe":
                print(f"{key.capitalize()}: {ingredients[key]}g")
            else:
                print(f"{key.capitalize()}: {ingredients[key]}")
        print(f"Money: ${'%.2f' % money}")

    def check_enough(current_amount: dict, option: str) -> str:
        requirements = MENU[option]["ingredients"]
        for ingredient in list(requirements):
            if requirements[ingredient] > current_amount[ingredient]:
                return ingredient
        return ""

    def process_coins(cost: float):
        inserted_coins = 0
        print("Please insert coins")
        for key in list(COINS):
            number_of_coins = ""
            while not number_of_coins.isdecimal():
                number_of_coins = input(f"How many {key}: ")
            inserted_coins += int(number_of_coins) * COINS[key]
        if cost > inserted_coins:
            return -1
        else:
            return inserted_coins

    def update_resources(current_amounts: dict, option: str):
        for key in MENU[option]['ingredients']:
            current_amounts[key] -= MENU[option]['ingredients'][key]
        return current_amounts

    money = 0
    current_resources = stock
    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        match prompt:
            case "off":
                return
            case "report":
                print_resources(current_resources, money)
            case "espresso" | "latte" | "cappuccino":
                enough_resource = check_enough(current_resources, prompt)
                if enough_resource == "":
                    payment = process_coins(MENU[prompt]["cost"])
                    if payment == -1:
                        print("Sorry that's not enough money. Money refunded.")
                        continue
                    else:
                        change = payment - MENU[prompt]["cost"]
                        print(f"Here is ${'%.2f' % change} in change.")
                        money += MENU[prompt]["cost"]
                        current_resources = update_resources(current_resources, prompt)
                        print(f"Here is your {prompt} ☕️\nEnjoy!")
                else:
                    print(f'Sorry there is not enough {enough_resource}.')
                    continue

            case _:
                print("incorrect input")


coffe_machine(resources)

