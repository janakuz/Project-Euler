def fac(n):
    if (n > 1):
        return n*fac(n-1)
    else:
        return 1

print sum([int(x) for x in str(fac(100))])
