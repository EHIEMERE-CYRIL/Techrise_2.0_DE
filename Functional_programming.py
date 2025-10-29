# FUNCTIONAL PROGRAMMING

# def greet ():
#     greet = "Hello" #Body of the function
#     return greet
# y = greet
# print(y) #The instruction given to python

# greet()

# n = 4
# m = 5
# def multi(n, m): #takes two numbers n and m
#     '''This is for documentation'''
#     print(n*m)

# multi(n,m)

# Name = "Mike"
# print(Name)

# def People_Names(Names):
#     print(f"This is a guys name : {Names}")

# People_Names(Name)

# def names(name):
#     print(name)

#name("Mike") 

# def fruits (fruit1, fruit2):
#     print(f"I like {fruit1}. But I love {fruit2}")
# print("Banana","Udara")

# x = fruits("Banana","Udara")
# # print(x)
# # print(f"The fruit I love is in {x}")
# return



# def add (n,m):
#     return n + m
# y = add (6,2)
# print(y)

# def discount(Price, Percentage):
#     discount = Price * (Percentage/100)
#     Discounted_price= Price - discount
#     return Discounted_price
# y = discount(24, 67)
# print(y)
# print(discount) #Local Variable for function

# def plus(*arguments):
#     total = sum(arguments)
#     return total 
# y = plus (10,20,30)
# print(y)

# def user_prof(**details):
#     profile = {}
#     for key,value in details.items():
#         profile[key] = value
#     return profile
# User = user_prof(Name = "Chinonye")
# print(User)

# def multiply(a,b=2):
#     return a*b
# print(multiply(5))

# r1 = range(2,8)

def get_age(Name):
    '''This functions gets your age'''
    user_age = input("How old are you? ") # gets user age
    return f"{Name}, you are {user_age} old."

# print(get_age("Chima"))





    




