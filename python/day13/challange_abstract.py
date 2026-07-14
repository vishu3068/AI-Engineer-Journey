from abc import ABC, abstractmethod
class payment(ABC):

    @abstractmethod
    def pay(self):
        pass
class creditcard(payment):
    def pay(self):
        print('paid using credit card')
class UPI(payment):
    def pay(self):
        print('paid using UPI')
class cash(payment):
    def pay(self):
        print('paid using cash')

p1=creditcard()
p2=UPI()
p3=cash()

p1.pay()
p2.pay()
p3.pay()
