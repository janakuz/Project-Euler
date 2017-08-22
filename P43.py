res = 0

digitA = [x for x in range(1,10) if x != 5]
for a in digitA:
    digitB = [0] + [x for x in digitA if x != a]
    for b in digitB:
        digitC = [x for x in digitB if x != b]
        for c in digitC:
            digitD = [x for x in digitC if x % 2 == 0 and x != c]
            for d in digitD:
                digitE = [x for x in digitC if x != d and x != c and (c+d+x)%3==0]
                for e in digitE:
                    f = 5 #def divisible by 5
                    digitG = [x for x in digitC if x !=c and x != d and x != e and (e*100+f*10+x)%7==0]
                    for g in digitG:
                        digitH = [x for x in digitC if x != c and x != d and x != e and x != g and (f*100+g*10+x)%11==0]
                        for h in digitH:
                            digitI = [x for x in digitC if x != c and x != d and x != e and x != g and x != h and (g*100+h*10+x)%13==0]
                            for i in digitI:
                                digitJ = [x for x in digitC if x != c and x != d and x != e and x != g and x != h and x != i and (h*100+i*10+x)%17==0]
                                for j in digitJ:
                                    num = j+i*10+h*100+g*1000+f*10**4+e*10**5+d*10**6+c*10**7+b*10**8+a*10**9
#                                    print num
                                    res += num
                    
                    
