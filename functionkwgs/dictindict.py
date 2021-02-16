student={
    1000:{"id":1000, "name":"Joel", "course":"django","qualiication":"Btech"},
    1001: {"id": 1001, "name": "Ben", "course": "django", "qualiication": "Btech"},
}
# print(student)
# id=int(input("Enter id"))
# property=input("Enter property")
# if id in student and property in student[id]:
#     print(student[id][property])
# else:
#     if id in student:
#         print("id is present but property not present")
#     else:
#         print("id is not present")

# print(student[1000])
#
# emp={1:"Ben","age":20}
# print(emp[1])

def get_student(**kwargs):
    id=kwargs['id']

    if id in student:
        print(student[id]['name'])
        if 'property' in kwargs:
            property = kwargs['property']
            if property in student[id]:
                print(student[id][property])
            else:
                print("check the name of property")
    else:
        print("check id")

get_student(id=1000,property='course')

