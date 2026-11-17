class BalanceError(Exception):
    pass


balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

try:
    if amount > balance:
        raise BalanceError("Insufficient balance")
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)
except BalanceError as e:
    print(e)
