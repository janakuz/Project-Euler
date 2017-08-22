import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

i = 33
primes = [x for x in range(33) if isPrime(x)]
found = False

while (not found):
    fulfilled = False
    i += 2
    if (isPrime(i)):
        primes += [i]
    else:
        for p in primes:
            diff = i - p
            diff = diff/2.0
            if (math.sqrt(diff)==int(math.sqrt(diff))):
                fulfilled = True
                break
        found = not fulfilled
