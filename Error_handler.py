# Retirement age calculator

# Worker_age = input("Enter worker age: ").strip()
# if Worker_age.isdigit():
#     age = int(Worker_age)
#     retirement_age = age + 35
#     print(retirement_age)
# else:
#     print("Type in figures")

# try:
#     value = int(input("Enter a number: "))
#     result = 100 / value
#     print(result)
# # except ValueError:
# #     print("You must enter a valid number.")
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except ValueError:
#     print("Enter number in figures")
# finally:
#     print('😊')

# try:
#     Worker_age = input("Enter worker age: ").strip()
#     if not Worker_age.isdigit():
#         raise ValueError("Enter age in figure")
#     age = int(Worker_age)
#     if not 18 <= age <= 25:
#         raise ValueError ("Worker's age must be between 18 and 25")
# except ValueError as e:
#     print(f"Enter correct information: {e}")
# else:
#     retirement_age = age + 35
#     print(f"You will retire at age {retirement_age} years old")
# finally:
#     print('👍')


# General structure for exceptions: Using one try and except

'''
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file...)
    '''


'''Even numbers collection'''

class ZeroError(Exception):
    '''This is the error raised if the number is zero'''
Even_numbers = []
counter = 0

while True:
    try:
        User_numbers = input("Enter number: ").strip() # To input numbers and remove spaces
        counter += 1
        if counter == 5:
            break
        if not User_numbers.isdigit(): # This is incase the user inputs in words instead of figures
            raise ValueError("Enter number in figure")
        number = int(User_numbers) #convert to interger if not in interger
        if number == 0:
            raise ZeroError("Number is 0")
        if not 2 <  number:
            raise ValueError("Number must be above 2")
    except ZeroError as z:
        print(f"Enter number above 0: {z}")
    except ValueError as e:
        print(f"Enter correct number: {e}")
        break
    else:
        if number % 2 == 0:
            Even_numbers.append(number)
            print(Even_numbers)
        else:
            print("Not even")

    
        
            


    
    






