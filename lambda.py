students = [
    {"Name" : "Harry", "House" : "Gryffindor"},
    {"Name" : "Ron", "House" : "Gryffindor"},
    {"Name" : "Draco", "House" : "Slytherin"}
]

def f(students):
    return students["Name"]

students.sort(key=f)

print(students)