import itertools as it

found = False
i = 5
checked = {}

def isPerfectCube(n):
    return int(round(n**(1.0/3)))**3 == n

def tupleToInt(t):
    e = len(t)-1
    n = 0
    for d in t:
        n += d*10**e
        e -= 1
    return n

while (not found):
    wp = i**3
    digits = []
    while (wp > 0):
        digits += [wp % 10]
        wp /= 10
    digits = sorted(digits, reverse=True)
    maxPerm = tupleToInt(digits)
    if (maxPerm in checked):
        checked[maxPerm][0] += 1
        if (checked[maxPerm][0] == 5):
            found = True
    else:
        checked[maxPerm] = [1, i]
    if (found):
        print checked[maxPerm][1]**3
    i += 1

