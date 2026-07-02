count = 1
with open('student.txt', 'r') as file:
    for i in file:
        print('student',count,':', i.strip())
        count+=1
        