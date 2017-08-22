import math

def sumOfDivisors(n):
    sumOfDivs = 0
    for i in range(1, int(math.sqrt(n))+1):
        if (n % i == 0):
            sumOfDivs += i
            if (n/i != i and n/i < n):
                sumOfDivs += n/i
    return sumOfDivs

sumAmicable = 0
for i in range (2, 10000):
    if (sumOfDivisors(sumOfDivisors(i)) == i and sumOfDivisors(i) != i):
        print i
        sumAmicable += i
