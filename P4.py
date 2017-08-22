def lenInt(n):
    l = 0
    while (n > 0):
        n = n/10
        l += 1
    return l

def isPalindrome(n):
    l = lenInt(n)
    for i in range(1, l, 2):
        if ((n / 10**(l-i)) % 10 != n % 10):
            return False
        n = n/10
    return True

def largestPalindrome():
    maxPal = 0
    for i in range(100,999):
        for j in range(100,999):
            if (isPalindrome(i*j) and i*j > maxPal):
                maxPal = i*j
    return maxPal
