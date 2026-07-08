class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,marks):
        self.marks=marks
        super().__init__(name)

    def display(self):
        print('name: ',self.name)
        print('marks: ',self.marks)
st1=student('vishwanth',95)

st1.display()
