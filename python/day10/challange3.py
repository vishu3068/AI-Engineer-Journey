class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        print('name: ',self.name)
        if self.marks>=90:
            print('grade:A')
        elif 89>self.marks>=80:
            print('grade:B')
        elif 79>self.marks>=70:
            print('grade:C')
        else:
            print('fail')
s1=student('vishwanth',91)
s2=student('abhi',82)
s3=student('vijay',77)
s4=student('lasya',68)
s1.grade()
s2.grade()
s3.grade()
s4.grade()