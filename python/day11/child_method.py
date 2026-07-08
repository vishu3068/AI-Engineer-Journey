class person:
    def walk(self):
        print('person is walking')
class student(person):
    def study(self):
        print('student is studying')

s1=student()
s1.walk()
s1.study()