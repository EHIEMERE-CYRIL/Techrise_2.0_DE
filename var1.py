# print(2+2)
x1 = 10
# x2 = 6
# y = x1 + x2
# y = 6
# print(y)
#LESSON ON PYTHON DATA TYPES
# name = "Cyril" 
# print(name)
# x = [1,2,3]
# print(x)
# print(x[0])
# names = ["Chikodi","Cyril","Darlington","Uche","Ehiemere"]
# print(names)
# print(names[3])
# print(names[1:4])
# names[0] = "Kingsley"
# print(names)
# names[2] = "Chinedu"
# print(names)
# Fruits = ("Banana","Apple","Guava","Tangerine","Pawpaw")
# print(Fruits)
# Fruits(2) = "Watermelon"
# print(Fruits)
# print(Fruits[2])
# r = range(1,100,20)
# for i in r:
# #     print(i) 
# v = ["apple","banana","cherry"]
# for i in range(len(v)):
# #     print("fruit is good for you")
# dict1 = {"name":"Alice","age":20,"weight":42.5,"subjects":["Maths,Science"]}
# print(type(x1))
# # print(dict["nam e"]) #Accessing values by key
# dict1["name"] = "Chinedu" #Modifying value
# print(dict1)
# print(type(int(x1)))
# print(type(str(x1)))
# print(type(float("3.56")))
# txt = "The best things in life are free"
# if "free" in txt:
#     print("yes, 'free' is present")
# if "things" in txt:
#     print("yes, 'things' is present")
# txt = "The best things in life are free!"
# print("expensive" not in txt)
# a = "Hello, Word!"
# print(a.upper())
# print(a.lower())
# print(a.upper().lower())
# var1 = "'obi is a boy'"
# print(var1)
# string1 = "12345"
# num1 = int(string1)
# print("Hello World")
# string1 = "Chikodi is good"
# print(type(string1))
# number1 = 256
# print(type(number1))
# complex1 = 3+2j
# print(type(complex1))
# list1 = ['ada','obi','nonye']
# print(type(list1))
# dict1 = {"name":"chinonye","age":20}
# print(type(dict1))
# tuple1 = ("banana","apple",245,"chinonye")
# float1 = 0.34
# print(type(float1))
# r1 = range(5)
# print(r1)
# print(type(r1))
# list1 = ["Obi","Ada",26,37,55,"grace",20,36]
# print(list1[2::])
# print(string1 * 2)
# str1 = "Hello"
# str2 = "World"
# print(str1 +' '+ str2)
# str1 = "I am a man"
# print(str1[3:])
# Tup1 = (2,3,5,7,9)
# Tup1 =list(Tup1)
# print(Tup1)
# Tup1[2]= 35
# Tup1= tuple(Tup1)
# print(Tup1)
# list1.append(5)
# print(list1)
# list1.pop(5)
# print(list1)
# list1.pop()
# print(list1)
# range(5)
# print(range(5))
# dict1 = {'name':'obi', 'age':25, 'gender':'male'}
# print(dict1)
# dict1['name'] = 'Chinatu'
# print(dict1)
# set1 = {2,3,3,5,7,5,9,2}
# print(set1)
# set2 = {'ada','grace','Ada','mike'}
# # print(set2)
# print(ord("A"))
# name = "alice olisa"
# print(name.upper())
# print(name.capitalize())
# print(name.endswith("e"))

# print(name.split(" ")) #To separate 2 names, changing each to list
# print(name.split(" ")[0])
# print(name.split(" ")[1])
# print(name.replace("alice","emeka")) #replace alice with emeka after definining a new variable

# x = 'Hello' + ' World'
# print(x)
# y = "Hello" "World" *3
# print(y)

# x = [2,3,4,5,6,7]
# print(len(x))
# print(len(y))

# Lst = ["apple", "banana", "avacado"]
# Lst.append("pineapple") #to add an item to the list
# print(Lst)

# Lst.insert(1, "orange") #To add an item to the exact position of choice on the list
# print(Lst)

# Lst.remove("banana") # to remove an item from the list
# print(Lst)

# Lst.pop() # To remove the last item on the list
# print(Lst)

#CONDITIONAL STATEMENTS AND LOOPS

# X = 10
# if X > 0:
#     print("x is positive")
# elif X == 0:
#     print("x is zero")
# else:
#     print("x is negative")

#LISTS AND LOOPS

# lst = [1,2,3,4,5,6,7,8,9,10]
# for num in lst:
#     # print(num * 4)
#     if num > 5:
#         print(num)

# rg = range(50)
# for even_num in rg:
#     if even_num % 2 == 0:
#         even_num+=2
#         print(even_num)

# even = []
# for i in rg:
#     if i % 2 == 0 and i>0:
#         even.append(i)
# even.append(50)
# print(even)

# for x in rg:
#     if x % 2 == 0:
#         x+= 2
#         even.append(x)
# # even.append(50)
# print(even)


HR = [150, 160, 110, 90, 100, 120, 91, 94, 96, 153, 200,270,20,16,112,115,125]
Newborn = []
Children = []
Adults = []
Outliers = []

for num in HR:
    if num >124 and num <154:
        Newborn.append(num)
    elif num >109 and num <121:
        Children.append(num)
    elif num >89 and num < 101:
        Adults.append(num)
    elif num <21 or num>159:
        Outliers.append(num)
print("Newborn", Newborn)
print("Children", Children)
print("Adults", Adults)
print("Outliers", Outliers)

