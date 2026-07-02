with open('student.txt','a') as file:
    file.write('\nAge:21')

name =input('enter your name: ')
with open('student.txt','a') as file:
    file.write(name +'\n')
print('append successful')
