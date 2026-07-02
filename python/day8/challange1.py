name = input('enter the name: ')
with open('student.txt', 'a') as file:
    file.write(name + '\n')
print('sucessful append')
