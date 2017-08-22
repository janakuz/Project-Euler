def isPandigital(n):
    digits = []
    for i in str(n):
        digits += [int(i)]
    for i in range(1, len(digits)+1):
        if (i in digits):
            digits.remove(i)
        else:
            return False
    return len(digits) == 0

res = 0
used = []
# 2 and 3 = 4
for i in range(10,99):
    multiplier = 100
    product = i*multiplier
    while (len(str(product)) <= 4):
        num = int(str(i) + str(multiplier) + str(product))
        if (isPandigital(num) and product not in used):
            used += [product]
            res += product
        multiplier += 1
        product = i*multiplier


            
# 1 and 4 = 4
for i in range(1,9):
    multiplier = 1000
    product = i*multiplier
    while (len(str(product)) <= 4):
        num = int(str(i) + str(multiplier) + str(product))
        if (isPandigital(num) and product not in used):
            used += [product]
            res += product
        multiplier += 1
        product = i*multiplier
