import math

def nextRotation(n):
    nlen = len(str(n))
    first = n / 10**(nlen-1)
    n = n - first*10**(nlen-1)
    n = n*10 + first
    return n


def isPrime(n):
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

count = 5
for i in range(13, 1000000):
    wi = i
    if (not ("0" in str(wi) or "2" in str(wi) or "4" in str(wi) or "6" in str(wi) or "8" in str(wi)) and isPrime(wi)):
        primes = 1
        while (nextRotation(wi) != i and isPrime(nextRotation(wi))):
            primes += 1
            wi = nextRotation(wi)
        if (primes == len(str(i))):
            count += 1
        
