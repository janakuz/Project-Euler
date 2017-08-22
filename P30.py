#largest number as sum of 5th powers = 9**5*len(9**5)

res = 0
for i in range(10, 9**5*len(str(9**5))):
    sumOfDigits = 0
    num = i
    while (num > 0):
        d = num % 10
        sumOfDigits += d**5
        num = num/10
    if (i == sumOfDigits):
        print i
        res += i
