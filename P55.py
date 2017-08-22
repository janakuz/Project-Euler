def isPalindrome(n):
    wn = str(n)
    l = len(wn)
    for i in range(l/2):
        if (wn[i]!=wn[l-i-1]):
            return False
    return True


def reverse(n):
    l = len(str(n))-1
    reverseN = 0
    while (n > 0):
        reverseN += (n % 10)*10**l
        n /= 10
        l -= 1
    return reverseN


count = 0

for i in range(1,10000):
    palindromeFound = False
    iteration = 1
    wi = i
    while (iteration < 50 and not palindromeFound):
        wi = wi + reverse(wi)
        if (isPalindrome(wi)):
            palindromeFound = True
        else:
            iteration += 1
    if (not palindromeFound):
        count += 1
