for i in range(3):
    for j in range(3):
        print(i,j)

#program 2

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

#program 3
rows = int(input('enter the number of rows:'))
columns = int(input("enter the number of columns: "))
symbol = input("enter the symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()