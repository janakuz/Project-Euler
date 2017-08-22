def factorial(n):
    if (n == 1):
        return 1
    else:
        return n*factorial(n-1)


def combinations(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0

for n in range(1, 101):
    r = 1
    while (r < n):
        if (combinations(n,r)>1000000):
            count += 1
        r += 1
