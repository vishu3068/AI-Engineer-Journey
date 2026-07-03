#Write a program that asks the user for two numbers.
#Divide them.
#If second number is zero
#Print
#Cannot divide by zero
try:
    num1 = int(input('enter the num1: '))
    num2 = int(input('eter the num 2: '))
    print(num1/num2)
except ZeroDivisionError:
    print('cannot divided by zero')
