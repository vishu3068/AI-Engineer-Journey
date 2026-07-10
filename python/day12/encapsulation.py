class bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def display_balnce(self):
        print('balance: ',self.__balance)
account=bankaccount(5000)
account.display_balnce()
print(account.__balance)