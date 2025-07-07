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
#5 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=38
i =0
while i < len(nums) :
    if(nums[i] == x):
        print(i)
    i +=1