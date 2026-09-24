from authenticate import login
import banking
from accounts import show_account, change_pin
from transactions import show_statements
from reports import account_summary
from verification import get_menu_choice


def atm_menu(accounts, account_no):
    while True:
        print("\nMAIN MENU")
        print("1. Check Balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Mini statement")
        print("6. Account Details")
        print("7. Change PIN")
        print("8. Account Summary")
        print("9. Logout")

        choice = get_menu_choice("Enter your choice: ", 1, 9)

        if choice == 1:
            banking.check_balance(accounts, account_no)
        elif choice == 2:
            banking.deposit(accounts, account_no)
        elif choice == 3:
            banking.withdraw(accounts, account_no)
        elif choice == 4:
            banking.transfer_money(accounts, account_no)
        elif choice == 5:
            show_statements(accounts, account_no)
        elif choice == 6:
            show_account(accounts, account_no)
        elif choice == 7:
            change_pin(accounts, account_no)
        elif choice == 8:
            account_summary(accounts, account_no)
        elif choice == 9:
            print("LOGGED OUT SUCCESFULLY.")
            break


def main():
    accounts = {
        '1234567890': {
            'name': 'dherya',
            'pin': '1707',
            'balance': 10000000.0,
            'transactions': []
        },
        '9876543210': {
            'name': 'shivans pandey',
            'pin': '8176',
            'balance': 50.0,
            'transactions': []
        }
    }

    print("WELCOME TO THE ATM")
    account_no = input("Enter your account number:").strip()
    pin = input("Enter your PIN:").strip()

    if login(accounts, account_no, pin):
        print("LOGIN SUCCESFULLY.")
        atm_menu(accounts, account_no)
    else:
        print("INVALID ACCOUNT NUMBER OR PIN.")


if __name__ == "__main__":
    main()