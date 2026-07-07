class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print('name: ',self.name)
        print('salary: ',self.salary)

emp_1= employee('vishwanth',50000)
emp_2=employee('abhi',60000)

emp_1.display()
emp_2.display()