import math
import sys

def pentagonal(n):
    return n*(3*n-1)/2

def isPentagonal(n):
    return (math.sqrt(24*n+1)==int(math.sqrt(24*n+1)) and (math.sqrt(24*n+1)+1)%2==0 and (math.sqrt(24*n+1)+1)%3==0)

j = 1
k = 2

pj = pentagonal(j)
pk = pentagonal(k)

#has to be first number that satisfies condition since difference increases linearly with index
while(not isPentagonal(pk-pj) or not isPentagonal(pk+pj)):
    j = 1
    pj = pentagonal(j)
    k += 1
    pk = pentagonal(k)
    while (j < k and (not isPentagonal(pk-pj) or not isPentagonal(pk+pj))):
        j += 1
        pj = pentagonal(j)

minD = pk-pj
