import re

def pin_verification(pin):
    pattern = r"^[0-9]{4}$"
    return re.match(pattern, pin) is not None

def verify_account_number(account_no):
    pattern = r'^[0-9]+$'
    return re.match(pattern, account_no) is not None

def verify_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount <= 0:
                print("amont must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("please enter valid amount.")

def get_menu_choice(message, minimum, maximum):
    while True:
        try:
            choice = int(input(message))
            if minimum <= choice <= maximum:
                return choice
            print("enter a choice between", minimum, "and", maximum)
        except ValueError:
            print("please enter a valid number.")