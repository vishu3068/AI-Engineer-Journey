from abc import ABC, abstractmethod
class vehicles(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicles):
    def start(self):
        print('car started')
class bike(vehicles):
    def start(self):
        print('bike started')

c=car()
b=bike()

c.start()
b.start()
