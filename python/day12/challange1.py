class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary+=new_salary
        else:
            print('invalid salary')
e1=employee('vishwanth',3000)
e1.set_salary(5000)
e1.set_salary(-1000)
print(e1.get_salary())