class animal:
    def sound(self):
        print('animals makes the sound')
class dog(animal):
    def sound(self):
        print('dog barks')

dog1=dog()
dog1.sound()

#practise
class employee:
    def work(self):
        print('employee is working')
class developer(employee):
    def work(self):
        print('developer is writing the code')
d1=developer()
d1.work()