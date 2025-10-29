# Right Triangle of stars
def print_right_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  #move to next line

# Centered Pyramid of stars
def print_pyramid(rows):
    for i in range(1, rows + 1):
        #print spaces
        for s in range(rows - 1):
            print(" ", end="")
        #print stars
        for j in range(2 * i - 1):
            print("*", end="")
        print() #move to next line

# Numbers Pyramid
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print() # move to next line

print("Right Triangle:")
print_right_triangle(4)

print("\nPyramid")
print_pyramid(3)

print("\nNumber Pyramid:")
print_number_pyramid(3)