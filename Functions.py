#Function in Python
#is a block of statement that performs a specific tasks:
# def sum (a,b): 
#     return = a+b



# print(sum(7,7))
# print(sum(2,7))

# def avg (a,b,c):
#     a = a+b+c
#     av = a / 3
#     return av

# a =int(input("Enter number 1 "))
# b =int(input("Enter number 2 "))
# c =int(input("Enter number 3 "))

# print(avg(a,b,c))
# def cal_pro (a,b):
#     return a*b
# print(cal_pro(8,   9))


# li =[1,2,4,5,6,7,8,8]
# he =[1,8]
# def leng(list):
#     return print(len(list))

# (leng(li))
# (leng(he))

# hero = ["sidhu","tee","era"]
# def print_li(list):
#     for item in list:
#         print(item,end=" ")

# print_li(hero)
        
# def add(a):
#     if(a%2 == 0):
#         print("Number is Even")
#     else:
#         print("odd")
#     return a
# n = int(input("enter Number "))
# add(n)
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
n = int(input("enter number "))
cal_fact(n)