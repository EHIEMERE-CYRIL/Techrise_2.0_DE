#checks if a number is prime using a while loop

def is_prime(number): 
    if number <= 1:
        return False 
    
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False #if any divisor divides it evenly, it's not prime
        i += 1

    return True # if no divisor are found

def find_primes(start, end):
    primes = []
    current = start

    while current <= end:
        if is_prime(current):
            primes.append(current)
    return primes

print(find_primes(1, 20))