num = 1
den = 1
for k in range(33,0, -1):
    #1+1/(1+2k), every step but first: 1+1/(frac+2(k-x))
    num, den = den*2*k+num, den*(2*k+1)+num
    if (k > 1):
        #frac+1, unless last step, since there is no 1 left from upper level
        num, den = den, num + den

#add 2
num, den = 2*den+num, den

#sum digits in num
res = 0
for i in str(num):
    res += int(i)
