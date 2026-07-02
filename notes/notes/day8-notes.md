## day 8

## file handling
## what is file handling?
file handling is a built in funtion of python which is used to open, read, write,append etc and can perform many i/o operation.

## why use it?
in python once progra is exeuted memory will be clear out to store a file permanantly we use filehandling in python.

## file modes
read-'r'
write-'w'
append-'a'
create-'x'

## read()
read function is used to read the opened file and print content in it

## write()
write function is write or over write the opened file

## readline()
this function is used to read document line by line

# readlines()
this function is used to read multiple lines at once in the document

## append()
 this function is used information to the excisting files

# with open()
we can open file using 2 methods 
 1.open() function here wee need to close the file after using file with close()
 2.with open method here we need not to be close file it automatically closes by itself
 with open('sample.text', "r") as file: