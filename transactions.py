def add_transactions(accounts, account_no, transaction_type, amount):
    accounts[account_no]['transactions'].append((transaction_type, amount))


def show_statements(accounts, account_no):
    transactions = accounts[account_no]['transactions']
    print('\nMINI STATEMENT')
    if len(transactions) == 0:
        print('No transactions found.')
        return
    for number in range(len(transactions)):
        transaction_type = transactions[number][0]
        amount = transactions[number][1]
        print(number + 1, ".", transaction_type, ':', amount)
    print('Total transactions:', len(transactions))