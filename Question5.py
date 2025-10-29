# Variable scope challenge

#create a global variable counter initialized to 0
#create function increment_counter() that increments global counter
#create function get_counter() that returns current  counter value
#create function reset_cou(nter() that resets counter to 0

#global variable
counter = 0

def increment_counter():
    '''increment the global counter by 1'''
    global counter
    counter += 1

def get_counter():
    '''Return the current value of the global counter'''
    return counter

def reset_counter():
    '''Reset the global counter to 0'''
    global counter
    counter = 0

#Calling increment_counter() 5 times
print(f"Initial counter value: {get_counter()}")
for _ in range(5):
    increment_counter()

# Printing counter (shoulder be 5)
print(f"Counter after 5 increments: {get_counter()}")

# Calling reset_counter()
reset_counter()

#Printing counter (should be 0)
print(f"counter after reset: {get_counter()}")