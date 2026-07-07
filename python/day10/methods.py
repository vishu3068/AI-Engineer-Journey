class students:
    def __init__(self,name,marks,age):
        self.name = name
        self.marks=marks
        self.age= age
    def display(self):
        print('name: ',self.name)
        print('marks: ',self.marks)
        print('age: ',self.age)

s1=students('vishwanth',98,21)
s2=students('abhi',99,22)
s1.display()
s2.display()