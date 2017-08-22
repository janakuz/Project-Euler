import math

def sumOfDivisors(n):
    divisorSum = 0
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            divisorSum += i
            if (n/i != i and i != 1):
                divisorSum += n/i
    return divisorSum

def isAbundant(n):
    return (sumOfDivisors(n)>n)

abundantNumbers = []
for n in range(28124):
    if (isAbundant(n)):
        abundantNumbers += [n]

sumsOfAbundant = []
for i in abundantNumbers:
    for j in abundantNumbers:
        sumsOfAbundant += [i+j]

res = sum(list(set(range(28124)) - set(sumsOfAbundant)))
