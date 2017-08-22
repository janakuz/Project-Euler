diagonalSum = 1
s = 3
for i in range(1, 501):
    for step in range(1,5):
        diagonalSum += s
        s += i*2
    s += 2
