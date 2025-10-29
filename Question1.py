#Temperature converter function

#1. celsius_to_fahrenheit(celsius) - converts celsius to fahrenheit
#2. fahrenheit_to_celsius(fahrenheit) - converts fahrenheit to celsius

#Formular: F = (C * 9/5) + 32
#Formular: C = (F - 32) * 5/9


def celsius_to_fahrenheit(celsius):
    #converts temperature from Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32 #value of fahrenheit
    return(fahrenheit) #i.e returning the value of fahrenheit in the above

def fahrenheit_to_celsius(fahrenheit):
    #convert temperature from fahrenheit to celsius
    celsius = (fahrenheit - 32) * 5/9 #value of celsius
    return(celsius) #i.e returning the value of celsius in the above

print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(98.6))


