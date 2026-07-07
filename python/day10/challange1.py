class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print('area: ',self.length*self.breadth)

r1=rectangle(5,7)
r2=rectangle(9,7.9)

r1.area()
r2.area()