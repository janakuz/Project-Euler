import math

def isPrime(n):
    n = abs(n)
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True


maxN = 0
maxA = 0
maxB = 0
#b must be prime so expression is prime for n = 0
possibleB = [n for n in range(-999,1000) if isPrime(n)]
for a in range(-999, 1000):
    for b in possibleB:
        n = 0
        while (isPrime(n**2+a*n+b)):
            n += 1
        if (n > maxN):
            maxN = n
            maxA = a
            maxB = b
