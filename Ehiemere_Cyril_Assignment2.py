#PALINDROME

# import re

# def is_palindrome(text):
#     cleaned = re.sub(r'[^a-z0-9]','', str(text).lower()) # To remove spaces and transform all letters to lowercase
#     reversed_text = cleaned[::-1]
#     return cleaned == reversed_text
# def check_palindrome(value):
#     for value in value:
#         if is_palindrome(value):
#             print(f"{value} is a palindrome!")
#         else:
#             print(f"{value} is not a palindrome")

# Lst1 = [
#     'mummy',
#     'hannah',
#     'murder for a jar of red rum', 
#     'mom',
#     'seagull',
#     'tomato',
#     'no lemon, no melon',
#     'some men interpret nine memos',
#     'madam']
# check_palindrome(Lst1)


import time
#initialize empty lists
Lst1 = []
Lst2 = []

#function to collect user input into the lists
def get_user_list(list_name):
    list_data =[]
    while True:
        item = input(f"Enter a list data for {list_name}:")
        list_data.append(item)
        reply = input("Are you through:(yes/no):").strip().lower()
        if reply == "yes":
            break
    return list_data
    
#collect data for Lst1 and Lst2 lists
print("=== Populating Lst1 ===")
Lst1 = get_user_list("Lst1")

print("\n === Populating Lst2 ===")
Lst2 = get_user_list("Lst2")

#check if the two lists length matches
if len(Lst1) != len(Lst2):
    print("\n Length of lists does not match. program terminated!")
else:
    print("\n Lists Length matches. Proceeding",end="")
    for i in range(3):
        time.sleep(1)
        print(".",end="",flush=True)

#create dictionary
dict1 = dict(zip(Lst1,Lst2))
print("\n \n Dictionary created successfully")
print(dict1)
