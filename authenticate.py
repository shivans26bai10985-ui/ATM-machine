from verification import verify_account_number, pin_verification


def login(accounts, account_no, pin):
    if not verify_account_number(account_no):
        return False
    if account_no not in accounts:
        return False
    if not pin_verification(pin):
        return False
    if accounts[account_no]['pin'] == pin:
        print("Welcome, " + account_no)
        return True
    return False
