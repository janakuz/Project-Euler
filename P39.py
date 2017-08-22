import math

def gcd(a,b):
    while (b != 0):
        a, b = b, a % b
    return a

maxSolutions = 0
maxP = 0
for p in range(1, 1001):
    solutions = 0
    for m in range(1, 1+int(math.sqrt(p))):
        for n in range(1, m):
            if ((m-n) % 2 == 1 and gcd(m,n) == 1):
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                for k in range(1, p/2):
                    if (k*a+k*b+k*c==p):
                        solutions += 1
    if (solutions > maxSolutions):
        maxSolutions = solutions
        maxP = p

#VERY SLOW, IMRPOVE!
