import math

def gcd(a, b):
    while (b > 0):
        a, b = b, a % b
    return a

maxRatio = 0
maxN = 0

for n in range(12, 13):
    phin = n-1
    notRelPrime = []
    step = 1
    if (2**int(round(math.log(n,2))) == n):
        phin = n/2
    else:
        for i in range (2, 1+int(math.sqrt(n)), step):
            if (n % i == 0):
                phin -= len(range(1, n/i))
                if (n/i >= 1+int(math.sqrt(n))):
                    phin -= len(range(1,i))
                if (step == 1):
                    step = i
                else:
                    step += i
            print i, step
    print n, phin
    if (float(n)/phin > maxRatio):
        maxRatio = float(n)/phin
        maxN = n
