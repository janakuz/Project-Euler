import math

def isPrime(n):
    for i in range(2,1+int(round(math.sqrt(n)))):
        if (n%i == 0):
            return False
    return True

def nthPrime(n):
    i = 0
    p = 1
    while (i < n):
        p += 1
        if (isPrime(p)):
            i += 1
    return p
