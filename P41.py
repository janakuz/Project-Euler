import math

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, 1+int(math.sqrt(n))):
        if (n % i == 0):
            return False
    return True


# 1 + ... + 9 = 45
# 1 + ... + 8 = 36
# => 1-9 and 1-8 pandigitals can"t be prime
maxPrime = 0
digitsA = range(8)
for a in digitsA:
    digitsB = [x for x in digitsA if x != a and x != 0]
    if (a == 0):
        digitsB = [0] + digitsB
    for b in digitsB:
        digitsC = [x for x in digitsB if x != b and x != 0]
        if (b == 0):
            digitsC = [0] + digitsC
        for c in digitsC:
            digitsD = [x for x in digitsC if x != c and x != 0]
            if (c == 0):
                digitsD = [0] + digitsD
            for d in digitsD:
                digitsE = [x for x in digitsD if x != d and x != 0]
                if (d == 0):
                    digitsE = [0] + digitsE
                for e in digitsE:
                    digitsF = [x for x in digitsE if x != e and x != 0]
                    if (e == 0):
                        digitsF = [0] + digitsF
                    for f in digitsF:
                        digitsG = [x for x in digitsF if x != f and (x == 1 or x == 3 or x == 7)]
                        for g in digitsG:
                            num = a*10**6+b*10**5+c*10**4+d*10**3+e*10**2+f*10+g
                            if (isPrime(num) and num > maxPrime):
                                maxPrime = num
