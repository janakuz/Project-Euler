numbersInLetters = {1 : "one", 2: "two", 3: "three", 4: "four", 5: "five",
                    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                    15: "fifteen", 16: "sixteen", 17: "seventeen",
                    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
                    80: "eighty", 90: "ninety"}

count = 0
for i in range(1, 1001):
    n = i
    number = ""
    if (n == 1000):
        count += len("thousand") + 3
    if (n >= 100 and n < 1000):
        count += len(numbersInLetters[n/100]) + len("hundred")
        number += numbersInLetters[n/100] + " hundred "
        if (n%100 != 0):
            count += 3
            number += "and "
        n = n%100
    if (n >= 20 and n < 100):
        count += len(numbersInLetters[n-n%10])
        number += numbersInLetters[n-n%10]
        n = n%10
    if (n > 0 and n < 20):
        count += len(numbersInLetters[n])
        number += numbersInLetters[n]
#    print number

print count
        
