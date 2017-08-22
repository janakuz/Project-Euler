sundayCount = 0
sundayDate = 7
year = 1900
month = 1
while (year < 2001):
    sundayDate += 7
    if (month == 4 or month == 6 or month == 9 or month == 11):
        if (sundayDate > 30):
            month += 1
            sundayDate = sundayDate % 30
    elif (month == 2):
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            if (sundayDate > 29):
                month += 1
                sundayDate = sundayDate % 29
        else:
            if (sundayDate > 28):
                month += 1
                sundayDate = sundayDate % 28
    else:
        if (sundayDate > 31):
            month += 1
            sundayDate = sundayDate % 31
    if (month > 12):
        month = 1
        year += 1
    if (sundayDate == 1 and month != 13 and year > 1900):
        sundayCount += 1
