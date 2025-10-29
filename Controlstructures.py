# y = 10
# x = 5
# z = y+x
# print(z)

#CONDITIONAL CONTROL STRUCTURES
#IF is the key statement and its used only once
#ELSE is the second key statement
'''Structure for conditional statements
keyword, condition:
    Instruction to be executed
'''
# x = 15
# y = 3
# if y <=2:
#     print(x+y)  

# y = 3
# if y <=2:
#     print(x+y)
# else:
#     print(x*y)

#int1 = int(input('print enter the Number:'))
# if 10>= int1 <= 20:
#     print('Give the person a car')
# else:
#     print('try again later')
'''
if 20>=int1<=10:
    print('You won a car')
elif 40>=int1<=50:
    print('You won a van')
else:
    print('try again')
'''
# x = range(5)
# no = []
# for i in x:
#     print(i)


# dict1 = {
#     "name":"Chinedu",
#     "age": 18,
#     "class":"Junior",
#     "scores":[60,78,90,100]
#     }
# for key in dict1: #to print out keys only
#     print(key)

# for key in dict1.values(): #to print out values only
#     prin(t(key)

# r1 = range(1,13)
# for item in r1:
#     for item2 in r1:
#         print(f'{item} x {item2} = {item*item2}\n')
    

# r1 = 5
# for i in range(r1):
#     for j in range(i):
#         # print("*", end = " ")
#         print(i, end = " ")

# count = 0
# while count <=5:
#     print("God is good")
#     count += 1

# r1 = range(1, 13)
# for n in r1:
#     print(f"({n} times table)")
#     for m in r1:
#         print(f"{n} x {m} = {n*m}")
#     print()

#LOGICAL OPERATORS
#1. AND OPERATOR
# X = 5
# print(x>0 and x<10) #OUTPUT TRUE

# print(not(x>2 and x<10))# OUTPUT THE OPPOSITE OR REVERSE, THAT IS FALSE

#IDENTITY OPERATORS

# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits) 

# string1 = "obi is a boy" #INDEXING
# print(string1[0])

#FOR LOOP
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     # print(x)
#     if x == "banana":
#         continue
#     print(x)
    #     break 
    # print(x)

# for x in range(6):
#     print(x)
# else:
#     print("Finally finished")

# List1 = [10,0,25,-5,30,15,0,45]
# for n in List1:
#     if n < 0:
#         print("This one na negative integers o!!")
#         break

# for x in List1:
#     if x > 0:
#         print(x)
#     if x == 0:
#         print("E no dey for here")
#         continue
#     elif x < 0:
# #         print("We don jam bad error")
#         break

# List1 = [10,0,25,-5,30,15,0,45]
# List2 = []
# for x in List1:
#   if x > 0:
#     #  List2.append(x)
#   elif x == 0:
#      continue
#   elif x < 0:
#      continue
  
#   print(List2)

def print_multiplication_table(start, end, upto=10):
    for number in range(start, end + 1):
        print(f"\nMultiplication Table for {numbers}")
        print("-" * 25)
        for i in range(1, upto + 1):
            print(f"{number} * {i} = {number * i}")
print_multiplication_table(3, 5)
print()






    

