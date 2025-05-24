#Dictionary in python
# Dictionary are used to store data values in key:value pairs.
# They are unordered, mutable(changeable) and do not allow duplicates keys.
# dict ={
#     "name"  : "Ali",
#     "age"   : 22,
#     "marks" : [10, 20, 30, 40, 50],
#     "Uni"   : {"Gcuf layyah"}
# }
# dict["name"] = "asad"
# dict["Father"] = "Qayyum"
# print(dict)

# emp =[]
# emp.append({"name":"Ali", "age":22, "marks":[10,20,30,40,50], "Uni":{"Gcuf layyah"}})
# print(emp)
#no index 

# students = {
#     "name": "Asad",
#     "subjects": 
#         {"Math":65, "Physics":90, "Chemistry": 70}
# }
# print(students)

#nested dictionary

#Dictionary Methods
#dict(list)
#dist(values)
#dict.items()
student = {
    "name": "Ali",
    "age": 22,
    "marks": [10, 20, 30, 40, 50],
    "Uni": {"Gcuf layyah"}
}

# print(student.values())
print(student["name"])
print(student.get("name"))
