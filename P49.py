import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

def digits(n):
    digits = []
    while (n > 0):
        digits += [n % 10]
        n = n/10
    return set(digits)


found = False
i = 1488

while (not found and i < 10000):
    i += 1
    if (isPrime(i) and isPrime(i+3330) and isPrime(i+6660)
        and digits(i)==digits(i+3330) and digits(i)==digits(i+6660)):
        found = True
    
