import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

maxCount = 0
maxP = 0
ms = 0

for s in range(2,10): #<- CORRECT, but WHY???
    p = 0
    count = 0
    i = s
    while (p < 1000000):
        if (isPrime(i)):
            p += i
            count += 1
#            print "s", s, "i", i, "p", p
        i += 1
        if (isPrime(p) and count > maxCount):
            maxCount = count
            maxP = p
