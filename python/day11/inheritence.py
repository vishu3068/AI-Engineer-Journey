class animal:
    def eat(self):
        print('animal is eating')
class dog(animal):
    pass
d1=dog()
d1.eat()

#program 2
class person:
    def introduce(self):
        print('my name is vishwanth')
class student(person):
    pass
s1=student()
s1.introduce()