from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
        def sound(self):
            print('dog barks')
class cat(animal):
        def sound(self):
            print('cat meows')
    
d=dog()
d.sound()
c=cat()
c.sound()
