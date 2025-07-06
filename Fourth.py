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
# student = {
#     "name": "Ali",
#     "age": 22,
#     "marks": [10, 20, 30, 40, 50],
#     "Uni": {"Gcuf layyah"}
# }

# # print(student.values())
# print(student["name"])
# print(student.get("name"))
# Lecture ={
#     "teacher" : "Asad",
#     "class": {
#         "bio", "Chemistry" ,"Math" 
#     }
# }
# print(Lecture)

# dict = {
#     "name":"SK",
#     "cgpa": 2.9,
#     "college" : ["gc","Layyah"],
#     "isAdult" : True
# }
# dict['male'] = "yes"
# print(dict)


# null = {

# }
# null["name"] = "ASad"
# print(null)

# Student = {
#     "name": "ASAD",
#     "Subject":{
#         "Chem": 40,
#         "bio":53,
#         "phy": 90
#     },
#     "From": "layyah"   
# }

# Student.update({"name": "La"})
# print(Student)
# print("hi")

#Sets in Pyhton:
#set is the collection of the unordered items.
set = {1,2,3,4,5}
set.add("set is mutable")
print(set)
# Tuple:
tub= {
    "name": "Asad",
    "class": "BSCS"
}
tub.update({"name": "anwar"})
print(tub)
#Tuple is also mutable

li= [
    "asads", 23,"as"
]
li.append("talha")
print(li)
#List is also mutable 
tup = (1,2,3,4)
print(tup)
#Only tuble is not mutable