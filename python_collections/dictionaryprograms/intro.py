student = {"id": 1,"name":"Ben","age":20,"Name":"Ben"}
print(student)
student["name"]="Joe On"
print(student)
student.update({"name":"Rahul"})
print(student)
for item in student:
    print(item)
dict.update(student,{"Name":"Tony"})
print(student)
x=student.keys()
print(x)