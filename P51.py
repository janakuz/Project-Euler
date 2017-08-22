import math
import itertools as it

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

possibleNumbers = [x for x in it.product([0,1,2,3,4,5,6,7,8,9], repeat=5)
                   if x[0] != 0 and (x.count(0) == 3 or x.count(1) == 3
                                     or x.count(2) == 3)]
possibleNumbers += [x for x in it.product([0,1,2,3,4,5,6,7,8,9], repeat=6)
                   if x[0] != 0 and (x.count(0) == 3 or x.count(1) == 3
                                     or x.count(2) == 3)]


def checkPrimeGeneration(n):
    s = str(n)
    primeCount = 0
    start = 1
    if (s.count("1") == 3):
        start = 2
    elif (s.count("2") == 3):
        start = 3
    for i in range(start, 10):
        snew = s.replace(str(start-1), str(i))
        if (isPrime(int(snew))):
            primeCount += 1
    if (primeCount == 7):
        print n


for perm in possibleNumbers:
    e = len(perm)-1
    n = 0
    for i in perm:
        n += i*10**e
        e -= 1
    if (isPrime(n)):
        checkPrimeGeneration(n)
