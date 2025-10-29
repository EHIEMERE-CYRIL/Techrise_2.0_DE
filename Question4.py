# lambda Function exercise
#Using lambda funtion with filter() and map()

#Main list

Num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_nums = list(filter(lambda x: x % 2 == 0, Num1))

# Square all numbers
squared_nums = list(map(lambda x: x ** 2, Num1))

# Filter numbers greater than 50 from squared list
greater_than_50 = list(filter(lambda x: x > 50, squared_nums))

print("Even numbers: ", even_nums)
print("Squared: ", squared_nums)
print("Greater than 50: ", greater_than_50)