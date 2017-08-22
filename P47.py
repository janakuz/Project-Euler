import math

def distinctDivisors(n):
    wn = n
    count = 0
    for i in range(2, 1+int(math.sqrt(n))):
        divisor = False
        while(wn % i == 0):
            wn = wn/i
            divisor = True
        if (divisor):
            count += 1
    if (wn > int(math.sqrt(n))):
        count += 1
    return count


i = 646

while (not (distinctDivisors(i) == 4 and distinctDivisors(i+1) == 4
            and distinctDivisors(i+2) == 4 and distinctDivisors(i+3) == 4)):
    i += 1

##SLOW, MAYBE REVISIT
