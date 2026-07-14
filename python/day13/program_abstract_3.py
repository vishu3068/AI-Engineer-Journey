from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        print("Area = side × side")

class Circle(Shape):

    def area(self):
        print("Area = π × r × r")

Square().area()
Circle().area()


## program 4
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developer writes code")

class Manager(Employee):

    def work(self):
        print("Manager manages team")

Developer().work()
Manager().work()