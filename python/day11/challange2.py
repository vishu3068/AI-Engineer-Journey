class bankaccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        print('name: ',self.name)
        print('balance',self.balance)
class savingaccount(bankaccount):
    def __init__(self,name,balance,intrest_rate):
        self.intrest_rate=intrest_rate
        super().__init__(name,balance)
    def calculate_intrest(self):
        interest = self.balance * self.intrest_rate / 100
        print('intrest: ',interest)

acc1= savingaccount('vishwanth',10000,5)
acc1.calculate_intrest()
