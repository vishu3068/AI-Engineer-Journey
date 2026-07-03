def fun1():   # finally practise
    try:
        a=int(input('enter the number: '))
        b=int(input('enter the number: '))
        print(a/b)
        return 1
    except ZeroDivisionError:
        print('division by zero is not allowed!!')
        return 0
    except ValueError:
        print('invalid input!!!')
        return 0
    finally:
        print('runned succesfully')
x=fun1()
print(x)

age = int(input('enter the age:' ))

#raising error 
if age<18:
    raise Exception('age should be above 18')
print(age)


#practise inbuilt errors

try:
    file = open("abc.txt")

except FileNotFoundError:
    print("File does not exist.")


try:
    marks = int(input("Enter Marks: "))

except ValueError:
    print("Enter only numbers")