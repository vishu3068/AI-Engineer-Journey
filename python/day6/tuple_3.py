marks = (85,90,67,78,45,90,78,45,83,94,69,85,88)
#indexing
print(marks[3])
print (marks[-1])
print(marks.count(90))
print(marks.index(90))

#tuple concatination
marks1=(89,67,89,84,874,87,89,67,42,90)

total_marks= marks + marks1
print(total_marks)

#editing and adding elements into tuplre
temp = list(total_marks)
temp.append(59)
temp.remove(94)
temp[7] = 55
marks = tuple(temp)
print(marks)