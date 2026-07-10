class student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0<marks<100:
            self.__marks+=marks
        else:
            print('invalid marks')
s1=student(80)
s1.set_marks(95)
s1.set_marks(150)
print(s1.get_marks())
    