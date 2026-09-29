# ATM Management System

The project showcases a console-based application that enables an account holder to log in to his account, check his balance, deposit and withdraw money, transfer funds, view mini statement, update his PIN, etc. The system is implemented in Python.

## Features:

- Login with an account number and pin
- Enquiry of the balance
- Deposit cash
- Withdraw cash with insufficient balance validation
- Transfer funds
- View mini statement
- View account details
- Update the PIN with validation
- View account summary with total deposits and withdrawals

## The project structure:

The project consists of several files:
| File     | Description                 |
|--------------|----------------------------------------------|

| main.py   | The file with the main menu         |
| authenticate.py | The file to validate the user’s login and password |
| banking.py  | The file to perform the banking operations such as withdrawal, deposit, transfer, etc. |
| accounts.py | The file to work with accounts and manage PIN updates |
| transactions.py | The file to view the mini statement     |
| reports.py    | The file to view the account summary     |
| verification.py | The file to implement input validations  |
| test_atm.py | The file to test the correctness of the application |
## How to Launch the Application:
- Open the Terminal (in the project’s directory) and execute the command below:
```bash
python main.py
```

- Then enter the pin and account number.

Few sample accounts are defined in the application:

Account number: `1234567890`, pin: `1707`
Account number: `9876543210`, pin: `8176`

Note: This is a simple demo project with several limitations. For instance, the app stores the account info in variables, not a database. Also, all operations are in the console, so it’s better not to use this project for a bank. It’s suitable for a student to learn how to build a banking system.
Input validations secure the app from crashes due to incorrect user input such as letters instead of numbers. The system checks if an account number consists of 10 digits and a PIN consists of 4 digits.
