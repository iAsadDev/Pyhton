#Loops :
#Loops are used to repeat instruction;
# i = 5
# while i >= 1:
#     i -= 1
#     print(i)
#1
# i = 0
# while i <=100 :
#     print(i)
#     i += 1
# #2
# i = 100
# while i >= 0 :
#     print(i)
#     i -= 1
#3
# i= 1
# n =int(input("Enter Number "))
# while i <= 10 :
#     print(i *n)
#     i += 1 

#4 Traverse 
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx = 0
# while idx < len(nums)  :
#     print(nums[idx])
#     idx +=1 
#Question No 5
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x=38
# i =0
# while i < len(nums) :
#     if(nums[i] == x):
#         print(i)
#     i +=1


# nums = [1,4,9,16,25,36,49,64,81,100]
# i =0
# while i < len(nums):
#     print(nums[i])
#     i +=1 

#Break and Continue
# i = 0
# while i <=5:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# li = [1,2,3]
# for el  in li:
#     print(el)

# movie =["apple", "abnana","grapes", "apple"]

# for el in movie:
#     print(el)
# tup =(1,2,3,4,5)
# for el in tup :
#     print(el)
# str = "apna"
# for char in str :
#     if(char == 'n'):
#         print("n found")
#         break
#     print(char)   

# nums = [1,4,9,16,25,36,49,64,81,100]
# for n in nums :
#     print(n)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter Number "))
# idx =0
# for s in nums :
#     if(s == x):
#         print(idx)
#         break
#     idx+=1

# Range() :
#linear Search:

# for el in range(1,101,3):
#     print(el)

# for n in range(100,0,-1):
#     print(n)


#Table Logic
# num = int(input("Enter Number "))
# for n in range(1,11):
#     print(num,"*", n ,"=",num *n)


#pass Statement

# for el in range(10):
#     pass
# print("pass")
# for el in range(100):
#     print(el)
# i=0
# if i >5:
#     pass
# print("Hello ")

# Let's Practice
# find the sum of first n numbers:
# n=5
# sum =0
# for i in range(1, n+1):
#     sum +=i
# print(sum)


# num = int(input("enter Number "))
# sum = 1
# i =1
# while i <= num:
#     sum *=i
#     i += 1
# print(sum)
#find factorail
# 
#  
# import math
# n=int(input("number: "))
# res = math.factorial(n)
# print(res)


