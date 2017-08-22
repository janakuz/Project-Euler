import math

def isPrime(n):
    if (n%2 == 0):
        return False
    else:
        for i in range(2, 1 + int(round(math.sqrt(n)))):
            if (n%i == 0):
                return False
    return True
    
def factors(n):
    i = 2
    factors = []
    while (n > 1):
        if (isPrime(i)):
            while (n%i == 0):
                n = n/i
            factors = factors + [i]
        i += 1
    
    return factors

def maxFactor(n):
    return max(factors(n))
