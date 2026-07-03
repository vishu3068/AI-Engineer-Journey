##Ask the user for age.
#If age is below 18
#Raise your own Exception
#Not Eligible
#Otherwise print
#Eligible

age = int(input('enter the age: '))
if age<18:
    raise Exception('not eligible')
else:
    print("eligible" )

