from verification import pin_verification

def show_account(accounts, account_no):
    account = accounts[account_no]
    print('ACCOUNT DETAILS')
    print('account number:', account_no)
    print('account holder:', account['name'])
    print('balance:', account['balance'])

def change_pin(accounts, account_no):
    old_pin = input("Enter current PIN:"). strip()
    if accounts [account_no]['pin'] != old_pin:
        print("incorrct current PIN.")
        return
    new_pin = input('enter new 4-digit PIN: ').strip()
    if not pin_verification(new_pin):
        print("New pin must contain exactly 4 digits.")
        return
    confirm_pin = input("Confirm new pin:").strip()
    if new_pin != confirm_pin:
        print("PIN does not match.")
        return
    accounts[account_no]['pin'] = new_pin

    print(" PIN CHANGED SUCCESSFULLY.")
