import math

t = 285
p = 165
h = 143

def isPentagonal(n):
    x = math.sqrt(24*n+1)
    return (x==int(x) and (x+1) % 2 == 0 and (x+1) % 3 == 0)

def isHexagonal(n):
    x = math.sqrt(8*n+1)
    return (x == int(x) and (x+1) % 4 == 0)

i = 287
tn = 40755 + 286

while (not isPentagonal(tn) or not isHexagonal(tn)):
    tn += i
    i += 1
