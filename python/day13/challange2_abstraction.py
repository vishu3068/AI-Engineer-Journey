from abc import ABC,abstractmethod

class appliance(ABC):
    @abstractmethod
    def operate(self):
        pass
class fan(appliance):
    def operate(self):
        print('fan is rotating')
class AC(appliance):
    def operate(self):
        print('AC is cooling')
class washingmachine(appliance):
    def operate(self):
        print('washing machine is washing clothes')

f=fan()
A=AC()
W=washingmachine()

f.operate()
A.operate()
W.operate()