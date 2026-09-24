from verification import verify_amount


def check_balance(accounts, account_no):
    balance = accounts[account_no]['balance']
    print("Your current balance: ", balance)


def deposit(accounts, account_no):
    amount = verify_amount("Enter amount to deposit:")
    accounts[account_no]['balance'] += amount
    accounts[account_no]['transactions'].append(('Deposit', amount))
    print("Deposit successful of:", amount)
    print("New balance:", accounts[account_no]['balance'])


def withdraw(accounts, account_no):
    amount = verify_amount("Enter amount to withdraw:")
    balance = accounts[account_no]['balance']
    if amount > balance:
        print("Insufficient balance.")
        return
    accounts[account_no]['balance'] -= amount
    accounts[account_no]['transactions'].append(('Withdrawal', amount))
    print("Withdrawal:", amount)
    print("Please collect your cash.")
    print("New balance:", accounts[account_no]['balance'])


def transfer_money(accounts, account_no):
    amount = verify_amount("Enter amount to transfer:")
    balance = accounts[account_no]['balance']
    if amount > balance:
        print("Insufficient balance.")
        return

    receiver_account = input("Enter receiver account number:").strip()
    if receiver_account not in accounts:
        print("Recipient account not found.")
        return

    accounts[account_no]['balance'] -= amount
    accounts[receiver_account]['balance'] += amount
    accounts[account_no]['transactions'].append(('Transfer', amount))
    accounts[receiver_account]['transactions'].append(('Received', amount))
    print("Transfer successful.")
    print("New balance:", accounts[account_no]['balance'])
