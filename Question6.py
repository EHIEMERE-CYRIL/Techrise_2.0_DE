#Write a function 
#print_multiplication_table(number, upto = 10) that:

#1. Takes a number and optional 'upto' parameter (default 10)
#2. Prints



def print_multiplication_table(number, upto=10):
    for i in range(1, upto +1):
        print(f"{number} * {i} = {number * i}")

#To test the function

print_multiplication_table(7)
print() #To add space between table

print_multiplication_table(3, 5)
