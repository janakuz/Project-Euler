#a=m**2-n**2, b=2mn, c=m**2+n**2
#m**2+mn=tripleSum/2, m and n coprime, m-n odd

import math

def gcd(a,b):
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    return a
            
def pythagoreanTriples(tripleSum):
    m = int(round(math.sqrt(tripleSum/2)))
    while (m>0):
        n = (tripleSum/2 - m**2)/float(m)
        print m, n
        if (int(n)==n and n > 0):
            return [m**2-n**2, 2*m*n, m**2+n**2]
        m -= 1
    return []
        
