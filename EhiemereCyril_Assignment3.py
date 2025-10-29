                          #ASSIGNMENT 3

'''QUESTION 1
Using the concept of for loop, do a multiplication table from one to twelve i.e over the range 1,3'''

# r1 = range(1, 13)
# for n in r1:
#     # print(f"({n} Times Table)") # To add a header to each times table(Its optional)
#     for m in r1:
#         product = n*m
#         print(f"{n} x {m} = {n*m}", end = "\t") 
#     print() # To add a blank line for separation between tables



'''QUESTION 2
Using the concept of while loop, write the code for a password checker. 
The code will initialize a password and allow the user to input a password into the system,
while the users password does not match the already initialized one after three attempts,
the user will receive a message to try again later. 
But if the users password matches the initialized password before the maximum attempts is exhausted,
the user receives a login successful message'''

#Initialize the true_password and max_attempts
true_password = "myworld123"
total_attempts = 0
max_attempts = 3

#Start the while loop to check the password
while total_attempts < max_attempts:
    user_password = input("Enter password: ") #command the user to enter their password
    if user_password == true_password: #checking for matched password
        print("Login successful") #output when matched
        break
    else:
        print("Try again later") # output when ummatched









