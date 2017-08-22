def digits(n):
    digs = []
    while (n > 0):
        digs += [n % 10]
        n /= 10
    return digs

maxProduct = 0
for i in range(10000):
    m = 1
    p = m*i
    digs = digits(p)
    products = [p]
    while (0 not in digs and len(digs) < 9 and len(digs) == len(set(digs)) and not any(x in digits((m+1)*i) for x in digs) and m <= 9):
        m += 1
        p = m*i
        digs += digits(p)
        products += [p]
    if (len(digs) == 9 and 0 not in digs and len(digs) == len(set(digs))):
        print products
        conp = ""
        for i in products:
            conp += str(i)
        product = int(conp)
        if (product > maxProduct):
            maxProduct = product
