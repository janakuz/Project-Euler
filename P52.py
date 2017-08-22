def digits(n):
    digits = []
    while(n > 0):
        digits += [n % 10]
        n /= 10
    return sorted(digits)


i = 1
conditionFulfilled = False

while(not conditionFulfilled):
    i += 1
    digs  = digits(i)
    if (digs==digits(2*i) and digs == digits(3*i) and digs == digits(4*i)
        and digs==digits(5*i) and digs==digits(6*i)):
        conditionFulfilled = True
        
        
