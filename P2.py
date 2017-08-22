def fibEvenSum():
    s = 0
    i = 1
    prev = 1
    while (i < 4000000):
        i += prev
        prev = i-prev
        if (i%2==0):
            s += i
    return s
