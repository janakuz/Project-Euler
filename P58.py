import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

#INEFFICIENT, CONSIDER REVISITING


n = 1
increment = 2
ratio = 1
primes = 0

while (ratio > 0.1):
    total = 2*increment + 1
    for i in range(4):
        n += increment
#        print n, isPrime(n)
        if (isPrime(n)):
            primes += 1
    ratio = float(primes)/total
#    print ratio, primes, total
    increment += 2
    

