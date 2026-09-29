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

Account number: `1234567890`, pin: `1234`
Account number: `9876543210`, pin: `4321`

Note: This is a simple demo project with several limitations. I have used really basics of python the string ,lists and dictionaries with if else conditions and for loops . this project can be used as reference on how an atm or a banking system works. The system checks if an account number consists of 10 digits and a PIN consists of 4 digits. I have uploaded some screenshots for interface and outputs of the code.

#screen shots
<img width="327" height="355" alt="Screenshot 2026-09-29 222311" src="https://github.com/user-attachments/assets/b0a2f52f-45ec-4996-8c79-5efe08021e65" />
<img width="356" height="347" alt="Screenshot 2026-09-29 222240" src="https://github.com/user-attachments/assets/64fbcaae-c0f3-4d3a-8632-a8acb9222012" />
<img width="267" height="388" alt="Screenshot 2026-09-29 222209" src="https://github.com/user-attachments/assets/88c4b6ac-f231-4f9d-b226-cd8e3f26694d" />
<img width="402" height="332" alt="Screenshot 2026-09-29 222143" src="https://github.com/user-attachments/assets/d4d3dd68-6abd-4d5c-92f9-2e32ae3a47b6" />
<img width="308" height="340" alt="Screenshot 2026-09-29 222053" src="https://github.com/user-attachments/assets/fa45671a-9354-417f-a76e-58c9fcbeca3b" />
<img width="346" height="312" alt="Screenshot 2026-09-29 222028" src="https://github.com/user-attachments/assets/49b2a3be-a50b-4fbe-aafe-ee6f42574042" />
<img width="390" height="352" alt="Screenshot 2026-09-29 222009" src="https://github.com/user-attachments/assets/a9f4ed8c-c827-4e7e-a936-aa0af6050cc4" />
<img width="1386" height="993" alt="Screenshot 2026-09-29 221936" src="https://github.com/user-attachments/assets/5b0fa6b3-733e-4c6f-a212-5af5ab518483" />
<img width="1918" height="1072" alt="Screenshot 2026-09-29 221604" src="https://github.com/user-attachments/assets/e6801557-7a70-455d-b51a-0bcab5c57c95" />

