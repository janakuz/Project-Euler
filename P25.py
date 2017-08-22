def indexForLength(l):
    i = 2
    prev = 1
    current = 1
    while(True):
        temp = current
        current += prev
        prev = temp
        i += 1
        if (len(str(current)) == l):
            return i
