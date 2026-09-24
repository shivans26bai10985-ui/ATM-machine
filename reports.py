def account_summary(accounts, account_no):
    account = accounts[account_no]
    transactions = account['transactions']

    total_deposits = 0
    total_withdrawals = 0

    for transaction in transactions:
        transaction_type = transaction[0]
        amount = transaction[1]
        if transaction_type == 'Deposit':
            total_deposits += amount
        elif transaction_type == 'Withdrawal':
            total_withdrawals += amount

    print('\nACCOUNT SUMMARY')
    print("Customer name:", account['name'])
    print('Account number:', account_no)
    print('Current balance:', account['balance'])
    print('Total deposits:', total_deposits)
    print('Total withdrawals:', total_withdrawals)
    print('Number of transactions:', len(transactions))