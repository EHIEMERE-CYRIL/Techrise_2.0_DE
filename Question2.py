

import math, statistics as stat

# formular for calculating mean(average)
'''sum of numbers/length of numbers'''
# formlar for calculating median
'''1. sort numbers in ascending order
2. check if length of numbers = even
3. if odd, mid num = median'''
#formular for calculating range
'''max numbers - min numbers'''
numbers = [10, 20, 30, 40, 50]

def  calculate_mean(numbers):
    '''Return the average(mean) of a list of numbers'''
    
    # Remembering that mean is the average of a list of numbers
    average = sum(numbers)/ len(numbers)
    return(average)


mean = calculate_mean(numbers)

print(mean)



def calculate_median(numbers):
    '''Return the median of a list of numbers'''
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2 

    if n % 2 ==0:
        return (sorted_numbers[mid] + sorted_numbers[mid -1]) / 2
    else:
        return sorted_numbers[mid]
    
median = calculate_median(numbers)

print(median)


def calculate_range(numbers):
    '''Return the range (max - min) of a list of numbers'''

    return max(numbers) - min(numbers)  

range = calculate_range(numbers)

print(range)


def calculate_sum(numbers):
    '''Return the sum of all numbers'''
    return sum(numbers)

sum = calculate_sum(numbers)

print(sum)