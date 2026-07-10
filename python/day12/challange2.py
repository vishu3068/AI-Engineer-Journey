class creditcard():
    def pay(self,amount):
        print(amount,"paid using credit card")
class upi():
    def pay(self,amount):
        print(amount,"paid using upi")
class cash():
    def pay(self,amount):
        print(amount,'paid using cash')

payments=[creditcard(),upi(),cash()]

for payment in payments:
    payment.pay(1000)
