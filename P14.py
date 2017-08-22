def generateNext(n):
    if (n%2 == 0):
        return n/2
    else:
        return 3*n+1

maxLength = 0
maxStart = 0
for i in range(1,1000000):
    count = 0
    n = generateNext(i)
    while(n != 1):
        count += 1
        n = generateNext(n)
    if (count > maxLength):
        maxLength = count
        maxStart = i

