def digitSum(n):
    s = 0
    while (n > 0):
        s += n % 10
        n /= 10
    return s


maxSum = 0

for a in range(2,100):
    for b in range(1,100):
        n = a**b
        digSum = digitSum(n)
        if (digSum > maxSum):
            maxSum = digSum
