##To find the last m digits of a number, calculate x mod 10**m
##In this case x = y * 2**n + 1. We know that y * 2**n mod a is congruent
##    to y mod a * 2**n mod a, and in this case y mod a = y
##2**n is congruent to 2**(m+j) where j = (n-m) mod 4*5**(m-1)
m = 10
y = 28433
n = 7830457
j = (n-m) % (4*5**(m-1))
res = (2**(j+m) % 10**m) * y
