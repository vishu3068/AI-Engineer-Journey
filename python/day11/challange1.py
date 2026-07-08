class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
            print('name: ',self.name)
            print('age: ',self.age)
class student(person):
    def __init__(self,name,age,marks):
        self.marks=marks
        super().__init__(name,age)
        
        
    def display_student(self):

        print('marks',self.marks)

        

st1=student('vishwanth',21,98)
st1.display_person()
st1.display_student()