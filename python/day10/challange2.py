class bankaccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print('name: ',self.name)
        print('balance: ',self.balance)
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,withdraw_amount):  
        if withdraw_amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance = self.balance - withdraw_amount

acc1=bankaccount('vishwanth',80)
acc1.display()
acc1.deposit(1000)
acc1.withdraw(10000)
acc1.display()