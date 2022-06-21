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

def check_resources(drink):
    ordered_drink = MENU[drink]['ingredients']
    if resources['water'] > ordered_drink['water'] and resources['milk'] > ordered_drink['milk'] and resources['coffee'] > ordered_drink['coffee']:
        return True
    return False

def check_payment(drink, quarters, dimes, nickles, pennies):
    sum_of_coins = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    change = sum_of_coins - MENU[drink]["cost"]
    if change >= 0:
        return change
    else:
        print("Sorry that´s not enough money. Money refunded")
        return False

def make_drink(drink, resources):
    ordered_drink = MENU[drink]['ingredients']
    for item in resources:
        resources[item] = resources[item] - MENU[drink]['ingredients'][item]
    return True

def print_report(money, resources):
    for item in resources:
        if item == 'coffee':
            print(f"{item.capitalize()}: {resources[item]}g")
        else:
            print(f"{item.capitalize()}: {resources[item]}ml")
    print(f"Money: ${money}")

def print_missing_resource(choice_of_drink, resources):
    ordered_drink = MENU[choice_of_drink]['ingredients']
    for item in resources:
        if resources[item] < ordered_drink[item]:
            print(f"Sorry there is not enough {item}!")
            return False

money = 0
machine_on = True
while machine_on:
    #Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    choice_of_drink = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 6.) Turn off the Coffee Machine by entering “off” to the prompt
    if choice_of_drink == "off":
        machine_on = False
    # TODO: 7.) Print report
    elif choice_of_drink == "report":
        print_report(money, resources)
    else:
        # TODO: 2.) Check resources sufficient?
        confirmation = check_resources(drink = choice_of_drink)
        if confirmation == False:
            printing_resources = print_missing_resource(choice_of_drink, resources)
        else:
            # TODO: 3.) Process coins.
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            payment_confirmation = check_payment(choice_of_drink, quarters, dimes, nickles, pennies)

            if payment_confirmation is not False and payment_confirmation != 0:
                money += MENU[choice_of_drink]["cost"]
                print(f"Here is {payment_confirmation} in change.")

            # TODO: 5.) Make Coffee.
            if payment_confirmation is not False and confirmation == True:
                make_drink(choice_of_drink, resources)
                print(f"Here´s your {choice_of_drink} ☕. Enjoy")

