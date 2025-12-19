# QUESTION 1
'''Write a NumPy program that creates an array of 20 random integers between 10 and 50. 
Then, calculate the sum, mean, standard deviation, and variance of the elements in the array and print them each'''

import numpy as np

# Create an array of 20 random integers between 10 and 50
Array_1 = np.random.randint(10, 51, size=20) #10 is the upper bound, 51 is the lower bound, and size=20 to genereate 20 integers would 
print("Array:", arr)

# Calculations
total_sum = np.sum(Array_1)
print("Sum:", total_sum)

mean_value = np.mean(Array_1)
print("Mean:", mean_value)

std_dev = np.std(Array_1)
print("Standard Deviation:", std_dev)

variance = np.var (Array_1)
print("Variance:", variance)


# QUESTION 2
'''Create a 2D NumPy array with random values between 5 and 15 with a shape of (4, 4). 
Use NumPy to find the minimum and maximum values both column-wise and row-wise'''

#Create a 4x4 NumPy array with random integers between 5 and 15
Array_2 = np.random.randint(5, 16, size=(4, 4))
print(Array_2)

# Row-wise (axis=1)
row_min = np.min(Array_2, axis=1)
print("\nRow-wise minimum:",row_min)

row_max = np.max(Array_2, axis=1)
print("Row-wise maximum:", row_max)

# Column-wise (axis=0)
column_min = np.min(Array_2, axis=0)
print("\nColumn-wise minimum:", column_min)

column_max = np.max(Array_2, axis=0)
print("Column-wise maximum:", column_max)

#QUESTION 3
'''Given a 1D array below, reshape this array into a 2D array with 3 rows and 4 columns. Print the reshaped array.
# ```python'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshape_array = np.reshape(arr, (3, 4))
print(reshape_array)

#QUESTION 4
'''Given a 2D array , resize this array to shape ```(3, 2)```. How does resizing differ from reshaping? Illustrate with the resulting array.
```python'''

array2D = np.array([[6, 8, 17, 16, 2],
                  [1, 6, 3, 9, 13]])
print(np.resize(array2D, (3, 2)))

#Difference between resizing and reshaping
#1. In reshaping, the number of elements is maintained and not altered(i.e, the number of elements in the initialized array must match with the reshaped one)
#WHILE In resizing, its not compulsory. Here, arrays are resized to suit any number of rows and columns specified.
#2. When reshaped arrays doesn't match the initialized arrays, it raises a value error. WHILE in resizing, it takes any size and mustn't be matched

#QUESTION 5
'''Create a ```3x4``` array of random integers between 1 and 20. Transpose the array and print both the original and transposed arrays.'''

Array_3 = np.random.randint(1, 21, size= (3, 4))
print(Array_3)
transpose_array = np.transpose(Array_3)
print(transpose_array)

#QUESTION 6
'''Given two 2D arrays below, concatenate these arrays along the rows ```(axis=0)``` and along the columns ```(axis=1)```. Print the results.
```python'''

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

#Concatenating along the rows
arr3 = np.concatenate((arr1, arr2), axis=0)
print(arr3)

#Concatenating along the columns
arr4 = np.concatenate((arr1, arr2), axis=1)
print(arr4)

#QUESTION 7
'''Create a 1D array of 12 elements. Split this array into 3 equal parts. Print each part.'''

array_1D = np.array([2, 3, 4, 5, 6, 7, 8, 9, 7, 10, 15, 18])

#Split into 3 equal parts (i.e 12 elements divided by 3, will give 4 elements for each part)
split_parts = np.split(array_1D, 3)
print(split_parts)

#To display the results in each parts
for i, part in enumerate(split_parts, 1): #For every splited arrays, assign it to a (variable) part, which will iterate through the splited parts starting from 1
    print(f"Part {i}: {part}") #format string to list the iterated splited arrays in parts.

#QUESTION 8
'''Given a 3D array below, flatten this array into a 1D array. Print the result.
```python'''

array_3D = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                
                [[7, 8, 9],
                 [10, 11, 12]]])
flatten_array = np.ravel(array_3D)
print(flatten_array)

#QUESTION 9
'''Given two 1D arrays below, stack these arrays vertically and horizontally. Print the results.
```python'''
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#To stack vertically
vertical = np.vstack((a, b))
print(vertical)

#To stack horizontally
horizontal = np.hstack((a, b))
print(horizontal)

#QUESTION 10
'''Create a 2D array of shape ```(3, 3)``` with all elements equal to 1. 
Add a 1D array of shape (3,) with elements ```[1, 2, 3]``` to this 2D array using broadcasting. Print the result.'''

#Create a 2D array of shape(3,3), with all elements equal to 1
array_2D = np.ones((3, 3), dtype=int)
print(array_2D)

#Create A 1D array of shape (3,) with elements [1,2,3] 
array_1D = np.array([1, 2, 3])
print(array_1D)

#Add using broadcasting
Outcome = array_2D + array_1D
print(Outcome)























