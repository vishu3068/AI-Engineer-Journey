class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount

account=bankaccount(5000)
account.deposite(1000)
print(account.get_balance())