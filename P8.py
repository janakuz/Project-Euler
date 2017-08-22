def seriesProd(n, l):
    s = str(n)
    maxProd = 0
    for i in range(len(s)-l):
        newProd = reduce(lambda x,y: int(x)*int(y), s[i:i+l])
        if (newProd > maxProd):
            maxProd = newProd
    return maxProd
