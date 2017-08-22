import math

def isPrime(n):
    for i in range(2,1+int(round(math.sqrt(n)))):
        if (n%i == 0):
            return False
    return True

def sumPrimes(n):
    i = 2
    s = 0
    while (i < n):
        if (isPrime(i)):
            s += i
        i += 1
    return s
