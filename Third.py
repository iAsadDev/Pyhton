# #List and Tuples 

# marks = [10, 20, 30, 40, 50]

# print(marks)
# print(len(marks)) 

# #List in python
# #A built in data type that is used to store
# #multiple values in a single variable
# #It can store elements of different data types(interger, float, string ,etc)

# Student = ["Asad" , 22 ,"Karor"]
# Student[1] = "Ali"
# # #string are immuteable means don't change 
# # #list is mutable  
# Student.append("Karachi")
# Student.reverse()
# Student.sort(reverse=True)
# Student.remove("Karachi")
# Student[1] =23
# print(Student)
# # Tuples  /////////////////
# #A tuple is a collection which is ordered and unchangeable.
# #Tuples allow duplicate members


# tub = (1,3,4,5,6,3)
# print(tub)
# print(tub[0])

# emp = ("Hello" ,"World", 1, 2, 1,1,4, 5)
# print(emp.count(1))
# print(emp)

# #Pracrtice Question
# movies = []
# m1= str(input("Enter movie name 1: "))
# m2= str(input("Enter movie name 2: "))
# m3= str(input("Enter movie name 3: "))

# movies.append(m1)
# movies.append(m2)
# movies.append(m3)


# print(movies)


# # Question no 2

# list=["m", "o" , "m"]
# copy = list.copy()
# copy.reverse()
# if(copy == list):
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")

# # Question no 3
# students = ["c","d" ,"a", "b","f","a","d"]
# print(students.count("a"))
# students.sort()
# print(students)
# #Question no 4:
# students = ["ali","ahmed","Asad"]
# print(students.count("ali"))


# Start python 
#List In Python:

# A built in data type that stored the sets of values:
# The values belongs to different Data types:
# Student = ["Ali" , 12, "Layyah"]
# Student.pop(0)
# print(Student)
#Tuples In Python:
mov = [
    input("Enter First Movie "),
    input("Enter Second Movie "),
    input("Enter Third Movie ")
]

print(mov)
# mov.append(movie1)
# mov.append(movie2)
# mov.append(movie3)
# mov.extend([movie1, movie2, movie3])
