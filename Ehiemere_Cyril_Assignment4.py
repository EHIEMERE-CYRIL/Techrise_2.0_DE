                        #ASSIGNMENT

'''1. Write a code to do the following: the code takes in two numbers A and B.
It then subtracts B from A if A is greater than B with the message"A-B='A-B'" 
where 'A-B' is the difference of A and B.
 If B is greater than A., it then subtracts A from B and gives the message"B-A='B-A'" 
 where 'B-A' the the difference between B and A.
 When both conditions are  negative, the program should give the corresponding message.'''


# a = int(input("What is A: "))
# b = int(input("What is B: "))

# if a > b:
#     b - a
#     print(f"A-B = {a-b}")
# elif b > a:
#     b - a
#     print(f"B-A = {b-a}")
# else:
#     print("A and B are equal")

'''2. Write a code to take in a string of any lenght. 
if there are spaces between words, they are removed.
non alphabetical characters are also removed. 
if the index of a particular alphabet is even, the program converts
it to a capital letter and if the index number is odd,  it is
converted to a small letter. the resulting string is then printed out'''


# Main_string = input("What is your location: ")

# Outcome_string = ""

# String_index = 0

# for item in Main_string:
#     if item.isalpha():
#         if String_index % 2 == 0:
#             Outcome_string += item.upper()
#         else:
#             Outcome_string += item.lower()
#         String_index += 1
# print(Outcome_string)

'''3. Okoro and sons company recently advertised vacancies. 
The number of applicants are much and have to be pruned
down while the successfull applicants are to be fixed in the following departments: 
Engineering, Admin, Customer Care and Security based on certain criteria. The company has 
a policy of not employing people that are not up to 18 years. 
Any man not up to 25 years old is placed in 
Customer care department. Any woman below 31 years is also
placed in the Customer care department. Any man below
45 years old is posted to the Engineering department. 
The rest of the women are posted to the Admin department.
The rest of the men are recruited as security men. 
All successful applicants should not exceed 50 years of age. 
write a code to place all the personnel in their various
departments accordingly immediately they make their 
application(if they are eligible) '''

# age = int(input("What is your age: "))

'''Engineering'''
'''Admin'''
'''Customer care'''
'''Security'''

# if age < 18 or age>50:
#     print("You are not eligible!")
#     exit()
# gender = input("What is your gender: ").lower()
# if gender == "male" and age >= 18 and age < 25:
#     print("You are in the customer care department?")
# elif gender == "female" and age <31:
#     print("You are in the customer care department!")
# elif gender == "male" and age >= 25 and age <45:
#     print("You are engineering department!")
# elif gender == "female" and age >= 31 and age <= 50:
#     print("You are in admin department!")
# elif gender == "male" and age >= 45:
#     print("Congratulation!!! You are in the security department")

# print("#" * 2)

# for i in range (4):
#     print("#", end = '')

for i in range (4):
    for j in range(4):
        print("#", end = ' ')
    print()
