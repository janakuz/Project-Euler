import math


def numDivisors(n):
    divs = 0
    for i in range(1, 1+int(round(math.sqrt(n)))):
        if (n%i==0 and n/i != i):
            divs += 2
        elif (n%i == 0 and n/i == i):
            divs += 1
    return divs

def triagNumWithNDivs(n):
    i = 1
    j = 2
    while (numDivisors(i) <= n):
        i += j
        j += 1
    return i
