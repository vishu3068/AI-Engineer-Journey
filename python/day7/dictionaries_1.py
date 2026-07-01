student = {
    "name": "Vishwanth",
    "branch": "AIML",
    "city": "Hyderabad"
}
print(student)
print(student["name"])
student["cgpa"] = 8.2
print(student)
student['cgpa'] = 9.0
print(student)
print(student.keys())
print(student.values())
print(student.popitem())
print(student.clear())