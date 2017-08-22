def findCommonDigit(m, n):
    digitsM = []
    for i in str(m):
        digitsM += [int(i)]
    for d in str(n):
        if (int(d) in digitsM):
            return int(d)
    return 0


def gcd(m, n):
    while (n != 0):
        n, m = m % n, n
    return m


fractions = []
for i in range(10, 99):
    for j in range(i+1,99):
        d = findCommonDigit(i,j)
        if (d != 0):
#            print i,j
            newI = 0
            newJ = 0
            
            digitsI = list(str(i))
            digitsI.remove(str(d))
            
            digitsJ = list(str(j))
            digitsJ.remove(str(d))
             
            for m in digitsI:
                newI += int(m)
            for n in digitsJ:
                newJ += int(n)
            if (j != 0 and newJ != 0 and float(i)/j == float(newI)/newJ):
                fractions += [(i,j)]

num = 1
den = 1
for f in fractions:
    num *= f[0]
    den *= f[1]

res = den/gcd(num,den)
