count = 0
# fractions represented as (numerator, denominator)
prev = (7,5)

for i in range(998):
    # new = (numerator + 2*denominator, numerator + denominator)
    prev = (prev[0] + 2*prev[1], prev[0] + prev[1])
    if (len(str(prev[0])) > len(str(prev[1]))):
        count += 1
    
