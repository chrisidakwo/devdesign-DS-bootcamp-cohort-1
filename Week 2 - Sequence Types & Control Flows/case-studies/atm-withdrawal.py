# A banking system needs to check if a customer has enough balance before allowing a withdrawal. 
# The ATM should also warn the user if their balance is low after the transaction.

print('')

accountBalance = 25000
lowBalance = 5000 #threshold

withdrawalAmount = input("Enter your withdrawal amount: ")

# Multi-nesting

# TODO: Ensure floats are handles with try/except
if not withdrawalAmount.isnumeric(): # Bug
    print('Please enter a valid figure!')
else:
    withdrawalAmount = float(withdrawalAmount)
    if accountBalance >= withdrawalAmount:
        accountBalance = accountBalance - withdrawalAmount
        if accountBalance <= lowBalance:
            print('Withdrawal successful. Account balance is low!')
        else:
            print('Withdrawal successful!')
    else:
        print('Insufficient funds! Withdrawal denied.')

print('')
