def digits(n):
    numdigits = 0
    while (n > 0):
        n /= 10
        numdigits += 1
    return numdigits
        

res = 1

for n in range(2,10):
    p = 1
    pown = n**p
    res += 1
    while (p <= digits(pown)):
        p += 1
        pown = n**p
        if (p == digits(pown)):
            res += 1        

