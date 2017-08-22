import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True

def truncateRight(n):
    return n / 10

def truncateLeft(n):
    if (n < 9):
        return 0
    return int(str(n)[1:])

tpLeft = 11
res = 0
i = 11
while (tpLeft > 0):
    if ((("0" not in str(i) and "2" not in str(i) and "4" not in str(i) and "6" not in str(i) and "8" not in str(i))
        or int(str(i)[0]) == 2) and isPrime(i)):
#    if (isPrime(i)):
        primes = 1
        wil = truncateLeft(i)
        wir = truncateRight(i)
        while (wil > 0 and isPrime(wil)):
            wil = truncateLeft(wil)
            primes += 1
        if (primes == len(str(i))):
            primes = 1
            while (wir > 0 and isPrime(wir)):
                wir = truncateRight(wir)
                primes += 1
                if (primes == len(str(i))):
                    tpLeft -= 1
                    res += i
    i += 2
