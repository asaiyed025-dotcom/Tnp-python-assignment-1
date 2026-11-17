class ATM:
    def __init__(self):
        self.__pin = "1234"
        self.__balance = 10000

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance =", self.__balance)
        else:
            print("Wrong PIN")

    def withdraw(self, pin, amount):
        if pin != self.__pin:
            print("Wrong PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")
            print("Balance =", self.__balance)


atm = ATM()

pin = input("Enter PIN: ")
atm.check_balance(pin)

amount = int(input("Enter amount to withdraw: "))
atm.withdraw(pin, amount)
