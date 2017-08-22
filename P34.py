def fac(n):
    if (n > 1):
        return n*fac(n-1)
    return 1

res = 0

# 2 digits
for i in range(1,5):
    for j in range(5):
       if (fac(i)+fac(j) == i*10+j):
           res += i*10+j

# 3 digits
for i in range(1,7):
    for j in range(7):
        for k in range(7):
            if (fac(i)+fac(j)+fac(k) == i*100+j*10+k):
                res += i*100+j*10+k
# 4 digits
for a in range(1,8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                if(fac(a)+fac(b)+fac(c)+fac(d) == a*1000+b*100+c*10+d):
                    res += a*1000+b*100+c*10+d

# 5 digits
for a in range(1,9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    if (fac(a)+fac(b)+fac(c)+fac(d)+fac(e) == a*10000+b*1000+c*100+d*10+e):
                        res += a*10000+b*1000+c*100+d*10+e
                    

for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if (fac(a)+fac(b)+fac(c)+fac(d)+fac(e)+fac(f) == a*100000+b*10000+c*1000+d*100+e*10+f):
                            res += a*100000+b*10000+c*1000+d*100+e*10+f
