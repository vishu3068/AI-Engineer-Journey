#Ask the user for a filename.
#Try opening it.
#If file doesn't exist
#Print
#File not found.
#Otherwise print
#File opened successfully.
file_name = input('enter the file name: ')
try:
    open(file_name)
except FileExistsError:
    print('file does not exist')
else:
    print('File opened successfully.')